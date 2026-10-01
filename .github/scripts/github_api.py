"""Small GitHub API client shared by the validator and the list generator.

In GitHub Actions it uses the workflow token (GITHUB_TOKEN or GITHUB_API_KEY).
Locally it can go through a wrapper script instead of a token in the
environment: set GH_API_SH to a script that takes `[-X POST] /path [json]` and
prints the response body (the maintainer's Keychain-backed helper does this).

It never sleeps for long: when the primary rate limit runs out it stops and
reports it, so callers can fall back to cached data instead of hanging.
"""
import json
import os
import subprocess
import threading
import time
import urllib.error
import urllib.request

API = "https://api.github.com"


class RateLimited(Exception):
    """The primary rate limit is exhausted; further calls would fail."""


class Client:
    def __init__(self):
        self.script = os.environ.get("GH_API_SH")
        self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_API_KEY")
        self.points_used = 0
        self.points_left = None
        self.rest_left = None
        self._lock = threading.Lock()

    @property
    def available(self):
        return bool(self.script or self.token)

    @property
    def via(self):
        return "script" if self.script else ("token" if self.token else "none")

    # --- transport -------------------------------------------------------
    def _request(self, method, path, body=None):
        """Returns (status, headers, parsed_json_or_None). Retries transient errors."""
        if self.script:
            args = ["bash", self.script]
            if method != "GET":
                args += ["-X", method]
            args.append(path)
            if body is not None:
                args.append(json.dumps(body))
            for intento in range(3):
                try:
                    out = subprocess.run(args, capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
                    return 200, {}, json.loads(out)
                except (ValueError, subprocess.TimeoutExpired):
                    time.sleep(2 + 3 * intento)  # 502/504 pages from GitHub are HTML; hung connections time out
            return 502, {}, None
        req = urllib.request.Request(
            API + path,
            method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "best-of-ai-markets",
            },
        )
        for intento in range(3):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    return r.status, dict(r.headers), json.load(r)
            except urllib.error.HTTPError as e:
                headers = dict(e.headers or {})
                if e.code in (403, 429) and headers.get("X-RateLimit-Remaining") == "0":
                    raise RateLimited(f"{path}: primary rate limit exhausted")
                if e.code in (502, 503, 504) or (e.code in (403, 429) and "Retry-After" in headers):
                    time.sleep(min(int(headers.get("Retry-After", 0) or 0), 60) or 2 + 3 * intento)
                    continue
                try:
                    return e.code, headers, json.load(e)
                except ValueError:
                    return e.code, headers, None
            except (urllib.error.URLError, TimeoutError):
                time.sleep(2 + 3 * intento)
        return 502, {}, None

    # --- REST ------------------------------------------------------------
    def rest(self, path):
        """GET a REST path. Returns (status, headers, data)."""
        status, headers, data = self._request("GET", path)
        if headers.get("X-RateLimit-Remaining"):
            self.rest_left = int(headers["X-RateLimit-Remaining"])
        if isinstance(data, dict) and "rate limit" in str(data.get("message", "")).lower():
            raise RateLimited(f"{path}: {data.get('message')}")
        return status, headers, data

    # --- GraphQL ---------------------------------------------------------
    def graphql(self, query, variables=None):
        """Runs a query; returns (data, errors). Adds rateLimit accounting.

        Secondary (burst) limits are waited out and retried; an exhausted
        primary limit raises RateLimited so callers can stop cleanly.
        """
        q = query.rstrip()
        assert q.endswith("}")
        q = q[:-1] + " rateLimit { cost remaining resetAt } }"
        for intento in range(4):
            status, _, out = self._request("POST", "/graphql", {"query": q, "variables": variables or {}})
            if not isinstance(out, dict):
                return None, [{"type": "TRANSPORT", "message": f"HTTP {status}"}]
            errors = out.get("errors") or []
            textos = " ".join([str(out.get("message", ""))] + [str(e.get("message", "")) for e in errors]).lower()
            if "secondary rate limit" in textos or "abuse" in textos:
                time.sleep(30 * (intento + 1))
                continue
            if "rate limit" in textos and ("exceeded" in textos or any(e.get("type") == "RATE_LIMITED" for e in errors)):
                raise RateLimited(f"GraphQL: {textos[:200]}")
            data = out.get("data") or {}
            rl = data.pop("rateLimit", None) or {}
            if rl:
                with self._lock:
                    self.points_used += rl.get("cost") or 0
                    self.points_left = rl.get("remaining")
            return data, errors
        return None, [{"type": "SECONDARY_LIMIT", "message": "secondary rate limit persisted"}]


def batched_repositories(client, ids, fields, batch=20, extra_vars=None, var_decl=""):
    """Fetches `fields` for many repos with aliased GraphQL queries.

    Returns {id: node | None | "NOT_FOUND"} where None means the request kept
    failing (unknown) and "NOT_FOUND" means GitHub says the repo does not exist.
    Failed batches are split in halves before giving up on single repos.
    """
    result = {}

    def run(lote, depth=0):
        q = "query" + (f"({var_decl})" if var_decl else "") + " {" + " ".join(
            f"r{j}: repository(owner: {json.dumps(x.split('/')[0])}, name: {json.dumps(x.split('/')[1])}) {{ {fields} }}"
            for j, x in enumerate(lote)
        ) + " }"
        data, errors = client.graphql(q, extra_vars)
        not_found = {e["path"][0] for e in errors if e.get("type") == "NOT_FOUND" and e.get("path")}
        hard = [e for e in errors if e.get("type") != "NOT_FOUND"]
        if data is None or (hard and not data):
            if len(lote) > 1 and depth < 5:
                m = len(lote) // 2
                run(lote[:m], depth + 1)
                run(lote[m:], depth + 1)
            else:
                for x in lote:
                    result[x] = None
            return
        for j, x in enumerate(lote):
            node = data.get(f"r{j}")
            result[x] = node if node else ("NOT_FOUND" if f"r{j}" in not_found else None)

    for i in range(0, len(ids), batch):
        run(ids[i:i + batch])
    return result
