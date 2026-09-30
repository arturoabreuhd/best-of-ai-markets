"""Validates projects.yaml on every pull request.

Checks: valid YAML, required fields, known categories and labels, no duplicate
github_id (case-insensitive), and that every github_id added by the PR exists
on GitHub and is not archived. Prints every problem and exits 1 if any.

Usage: python validar_projects.py projects.yaml [base_projects.yaml]
Env:   GITHUB_TOKEN (optional, raises the API rate limit), SKIP_NETWORK=1 to skip the existence check.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

import yaml


def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        return yaml.safe_load(f)


def repo_en_github(github_id):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{github_id}",
        headers={"Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return f"GitHub answered {e.code} (repo missing, private or mistyped)"
    if d.get("archived"):
        return "repo is archived"
    if d["full_name"].lower() != github_id.lower():
        return f"repo was renamed/moved: use `{d['full_name']}`"
    return None


def main():
    ruta = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else None
    errores = []

    try:
        datos = cargar(ruta)
    except yaml.YAMLError as e:
        print(f"::error file={ruta}::YAML does not parse: {e}")
        sys.exit(1)

    categorias = {c["category"] for c in datos.get("categories", [])}
    etiquetas = {l["label"] for l in datos.get("labels", [])}
    vistos = {}
    for i, p in enumerate(datos.get("projects") or [], 1):
        nombre = p.get("name") or f"project #{i}"
        gid = p.get("github_id")
        if not p.get("name"):
            errores.append(f"project #{i}: missing `name`")
        if not gid or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", str(gid)):
            errores.append(f"{nombre}: `github_id` must look like owner/repo (got {gid!r})")
        if p.get("category") not in categorias:
            errores.append(f"{nombre}: unknown category {p.get('category')!r}")
        for l in p.get("labels") or []:
            if l not in etiquetas:
                errores.append(f"{nombre}: unknown label {l!r}")
        if gid:
            clave = str(gid).lower()
            if clave in vistos:
                errores.append(f"{nombre}: duplicate github_id {gid} (also `{vistos[clave]}`)")
            vistos[clave] = nombre

    nuevos = set(vistos)
    if base and os.path.exists(base):
        try:
            nuevos -= {str(p.get("github_id", "")).lower() for p in (cargar(base).get("projects") or [])}
        except yaml.YAMLError:
            pass
    if os.environ.get("SKIP_NETWORK") != "1":
        for gid in sorted(nuevos):
            problema = repo_en_github(gid)
            if problema:
                errores.append(f"{gid}: {problema}")

    if os.environ.get("SKIP_NETWORK") == "1":
        print(f"{len(vistos)} projects checked (GitHub existence check skipped)")
    else:
        print(f"{len(vistos)} projects, {len(nuevos)} new or changed github_id checked on GitHub")
    for e in errores:
        print(f"::error file={ruta}::{e}")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
