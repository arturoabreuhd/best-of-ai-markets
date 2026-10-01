"""Runs the best-of 0.8.5 generator with GitHub data fetched in batches.

Why: best-of asks GitHub one project at a time (one GraphQL query, one REST
call for contributors, one page load for dependents) and sleeps 150 s after
every failed call. GITHUB_TOKEN allows 1,000 GraphQL points and 1,000 REST
requests per hour per repository, so a list of a few thousand projects runs out
of quota in the first hour and the job times out.

What this does instead (the generator itself is untouched; only its three
network functions are swapped):
  1. Repository metadata: aliased GraphQL queries of 10 repos (4 in parallel)
     with the same fields best-of requests. Release download counts come from a second, smaller
     query (latest 10 releases x 50 assets, 1 point per 10 repos) only for
     repos that have releases; older releases' downloads are not counted.
  2. Contributors and dependents: reused from the newest history/*_projects.csv;
     each run refreshes the projects missing there plus a rotating quarter of the
     list, within a request budget, and stops early if the quota runs low.
  3. No 150 s sleeps: a repo with no data stays without data, and the workflow's
     data check fails the run if too many come back empty.

Usage: python generar.py projects.yaml
Env:   GITHUB_API_KEY (Actions token) or GH_API_SH (local wrapper, see github_api.py).
       CONTRIB_MAX, DEPEND_MAX: refresh budgets (default 850 and 800; REST allows
       1,000 requests/hour and the dependents page is not an API call).
"""
import csv
import glob
import logging
import os
import re
import sys
import time
import types
import urllib.error
import urllib.request
import zlib
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import yaml
from addict import Dict
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from github_api import Client, RateLimited, batched_repositories  # noqa: E402

log = logging.getLogger("generar")

CAMPOS = """
name nameWithOwner description url homepageUrl createdAt updatedAt pushedAt diskUsage
primaryLanguage { name } licenseInfo { spdxId } stargazerCount
pullRequests { totalCount } forks { totalCount } watchers { totalCount }
masterCommit: defaultBranchRef { target { ... on Commit {
  committedDate recent_activity: history(since: $since) { totalCount } history { totalCount } } } }
repositoryTopics(first: 100) { nodes { topic { name } } }
openIssues: issues(states: OPEN) { totalCount }
closedIssues: issues(states: CLOSED) { totalCount }
releases(first: 100, orderBy: {field: CREATED_AT, direction: DESC}) {
  totalCount nodes { createdAt publishedAt tagName isDraft isPrerelease } }
"""
CAMPOS_DESCARGAS = """
releases(first: 10, orderBy: {field: CREATED_AT, direction: DESC}) {
  nodes { releaseAssets(first: 50) { nodes { downloadCount } } } }
"""
RESERVA_PUNTOS = 60   # GraphQL points left untouched for the rest of the workflow
RESERVA_REST = 100    # REST requests left untouched (branch, push, PR, release)


def leer_ids(ruta):
    with open(ruta, encoding="utf-8") as f:
        datos = yaml.safe_load(f)
    return [str(p["github_id"]) for p in datos.get("projects") or [] if p.get("github_id")]


def leer_historial(carpeta):
    """{github_id_lower: row} from the newest *_projects.csv, or {}."""
    archivos = sorted(glob.glob(os.path.join(carpeta, "*_projects.csv")))
    if not archivos:
        return {}
    with open(archivos[-1], encoding="utf-8") as f:
        return {r["github_id"].lower(): r for r in csv.DictReader(f) if r.get("github_id")}


def entero(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def rotacion(ids, historial, campo, maximo):
    """Projects to refresh: missing in history first, then this week's quarter."""
    semana = datetime.utcnow().isocalendar()[1]
    faltan = [i for i in ids if entero((historial.get(i.lower()) or {}).get(campo)) is None]
    turno = [i for i in ids if i not in faltan and zlib.crc32(i.lower().encode()) % 4 == semana % 4]
    return (faltan + turno)[:maximo]


def precargar_metadatos(cliente, ids, lote=10, hilos=4):
    """Batches of 10 repos (big repos make larger GraphQL queries time out), 4 at a time."""
    since = (datetime.now() - timedelta(days=_dias_recientes())).isoformat()
    datos = {}

    agotado = []

    def pedir(grupo, campos, tam, variables=None, decl=""):
        if agotado or (cliente.points_left is not None and cliente.points_left < RESERVA_PUNTOS):
            return {}
        try:
            return batched_repositories(cliente, grupo, campos, batch=tam, extra_vars=variables, var_decl=decl)
        except RateLimited as e:
            agotado.append(str(e))
            return {}

    with ThreadPoolExecutor(hilos) as ex:
        for parte in ex.map(lambda g: pedir(g, CAMPOS, lote, {"since": since}, "$since: GitTimestamp!"),
                            [ids[i:i + lote] for i in range(0, len(ids), lote)]):
            datos.update(parte)
        sin_datos = sum(1 for i in ids if not isinstance(datos.get(i), dict))
        log.info(f"metadata pass: {len(ids) - sin_datos}/{len(ids)} repos, {cliente.points_used} GraphQL points so far"
                 + (f"; stopped: {agotado[0]}" if agotado else ""))
        puntos_antes = cliente.points_used
        con_releases = [i for i, n in datos.items() if isinstance(n, dict) and n["releases"]["totalCount"]]
        for parte in ex.map(lambda g: pedir(g, CAMPOS_DESCARGAS, lote),
                            [con_releases[i:i + lote] for i in range(0, len(con_releases), lote)]):
            for gid, n in parte.items():
                if isinstance(n, dict):
                    for rel, extra in zip(datos[gid]["releases"]["nodes"], n["releases"]["nodes"]):
                        # GitHub sometimes returns null asset nodes; best-of would skip the release
                        rel["releaseAssets"] = {"nodes": [a for a in extra["releaseAssets"]["nodes"] if a]}
        log.info(f"downloads pass: {len(con_releases)} repos with releases, {cliente.points_used - puntos_antes} GraphQL points"
                 + (f"; stopped: {agotado[0]}" if agotado else ""))
    return datos


def _dias_recientes():
    from best_of import default_config
    return default_config.RECENT_ACTIVITY_DAYS


def contar_contribuidores(cliente, gid):
    """Same method as best-of: the last page number with per_page=1."""
    status, headers, _ = cliente.rest(f"/repos/{gid}/contributors?page=1&per_page=1&anon=True")
    if status != 200:
        return None
    paginas = [int(p) for p in re.findall(r"[?&]page=([0-9]+)", headers.get("Link", ""))]
    return max(paginas) if paginas else 1


def contar_dependientes(gid):
    """Same page and parsing as best-of; returns None on errors instead of 0."""
    req = urllib.request.Request(f"https://github.com/{gid}/network/dependents",
                                 headers={"User-Agent": "best-of-ai-markets"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise RateLimited("github.com dependents page: 429")
        return None
    except (urllib.error.URLError, TimeoutError):
        return None
    sopa = BeautifulSoup(html, "html.parser")
    total = 0
    for patron in (r"[0-9,]+\s+Repositories", r"[0-9,]+\s+Packages"):
        texto = sopa.find(string=re.compile(patron))
        if texto:
            n = re.search("([0-9,]+)", texto)
            if n:
                total += int(n.group(1).replace(",", ""))
    return total


def refrescar(nombre, ids, historial, campo, maximo, contar):
    valores = {i.lower(): entero((historial.get(i.lower()) or {}).get(campo)) for i in ids}
    hechos = 0
    for gid in rotacion(ids, historial, campo, maximo):
        try:
            n = contar(gid)
        except RateLimited as e:
            log.warning(f"{nombre}: stopped after {hechos} refreshes ({e})")
            break
        if n is not None:
            valores[gid.lower()] = n
        hechos += 1
    log.info(f"{nombre}: refreshed {hechos}, reused the rest from history")
    return valores


def main():
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO, stream=sys.stdout)
    ruta = sys.argv[1]
    cliente = Client()
    if not cliente.available:
        sys.exit("generar.py: no GITHUB_API_KEY / GH_API_SH; refusing to build a list without GitHub data")
    with open(ruta, encoding="utf-8") as f:
        carpeta = (yaml.safe_load(f).get("configuration") or {}).get("projects_history_folder") or "history"
    ids = leer_ids(ruta)
    historial = leer_historial(carpeta)
    t0 = time.time()

    metadatos = precargar_metadatos(cliente, ids)
    ok = sum(1 for n in metadatos.values() if isinstance(n, dict))
    log.info(f"metadata: {ok}/{len(ids)} repos in {time.time() - t0:.0f}s, {cliente.points_used} GraphQL points")

    if cliente.via == "token":
        def contribuidores(g):
            if cliente.rest_left is not None and cliente.rest_left < RESERVA_REST:
                raise RateLimited(f"REST quota low ({cliente.rest_left})")
            return contar_contribuidores(cliente, g)
        contrib = refrescar("contributors", ids, historial, "contributor_count",
                            int(os.environ.get("CONTRIB_MAX", 850)), contribuidores)
    else:  # the local wrapper does not expose the Link header
        log.info("contributors: local run, reusing history only")
        contrib = refrescar("contributors", ids, historial, "contributor_count", 0, None)
    def dependientes(g):
        time.sleep(0.5)
        return contar_dependientes(g)
    depend = refrescar("dependents", ids, historial, "github_dependent_project_count",
                       int(os.environ.get("DEPEND_MAX", 800)), dependientes)

    import best_of.integrations.github_integration as gi
    por_id = {k.lower(): v for k, v in metadatos.items()}

    def metadatos_de(_token, github_id, _since):
        n = por_id.get(github_id.lower())
        if not isinstance(n, dict):
            return None
        n = dict(n)
        n["stargazers"] = {"totalCount": n.get("stargazerCount")}  # for unpatched code paths
        return Dict(n)

    gi.request_metadata_from_github_api = metadatos_de
    gi.get_contributors_via_github_api = lambda github_id, _token: contrib.get(github_id.lower())
    gi.get_repo_deps_via_github = lambda github_id: depend.get(github_id.lower()) or 0
    gi.time = types.SimpleNamespace(sleep=lambda _s: None)  # no 150 s waits for repos without data

    os.environ.setdefault("GITHUB_API_KEY", "prefetched")  # best-of skips GitHub when unset
    from best_of import generator
    generator.generate_markdown(ruta, None, os.environ["GITHUB_API_KEY"])
    log.info(f"done in {time.time() - t0:.0f}s; GraphQL points used {cliente.points_used}, left {cliente.points_left}")


if __name__ == "__main__":
    main()
