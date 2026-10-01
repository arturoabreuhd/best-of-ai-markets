"""Validates projects.yaml on every pull request.

Checks: valid YAML, required fields, known categories and labels, no duplicate
github_id (case-insensitive), no duplicate project name (case-insensitive: the
best-of generator silently drops the second project with the same name), and
that every github_id added by the PR exists on GitHub, is not archived and uses
its current name. Prints every problem and exits 1 if any.

The existence check runs in batches of 20 repos per GraphQL query, so even
thousands of new entries take a few minutes and stay far below the
GITHUB_TOKEN limit of 1,000 points per hour. A repo that cannot be checked
counts as an error (fail closed).

Usage: python validar_projects.py projects.yaml [base_projects.yaml]
Env:   GITHUB_TOKEN (needed for the batched check; see github_api.py for the
       local alternative GH_API_SH), SKIP_NETWORK=1 to skip the existence check.
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from github_api import Client, RateLimited, batched_repositories  # noqa: E402


def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        return yaml.safe_load(f)


def revisar_en_github(ids):
    """Returns (errors, summary) for the given github_ids (original case)."""
    cliente = Client()
    if not cliente.available:
        return [f"cannot check {len(ids)} new repos: no GITHUB_TOKEN (set SKIP_NETWORK=1 to skip on purpose)"], ""
    try:
        res = batched_repositories(cliente, sorted(ids), "nameWithOwner isArchived", batch=20)
    except RateLimited as e:
        return [f"GitHub rate limit hit while checking new repos: {e}"], ""
    errores = []
    for gid in sorted(ids):
        node = res.get(gid)
        if node == "NOT_FOUND":
            errores.append(f"{gid}: repo not found on GitHub (missing, private or mistyped)")
        elif node is None:
            errores.append(f"{gid}: could not be checked (GitHub API kept failing); re-run the check")
        elif node["isArchived"]:
            errores.append(f"{gid}: repo is archived")
        elif node["nameWithOwner"].lower() != gid.lower():
            errores.append(f"{gid}: repo was renamed/moved: use `{node['nameWithOwner']}`")
    return errores, f" ({cliente.points_used} GraphQL points used)"


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
    vistos, original, nombres = {}, {}, {}
    for i, p in enumerate(datos.get("projects") or [], 1):
        nombre = p.get("name") or f"project #{i}"
        gid = p.get("github_id")
        if not p.get("name"):
            errores.append(f"project #{i}: missing `name`")
        else:
            clave_nombre = str(p["name"]).strip().lower()
            if clave_nombre in nombres:
                errores.append(
                    f"{nombre}: duplicate project name (also used by `{nombres[clave_nombre]}`); "
                    "best-of drops the second one, so make the names distinct"
                )
            nombres[clave_nombre] = gid
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
            original[clave] = str(gid)

    nuevos = set(vistos)
    if base and os.path.exists(base):
        try:
            nuevos -= {str(p.get("github_id", "")).lower() for p in (cargar(base).get("projects") or [])}
        except yaml.YAMLError:
            pass

    if os.environ.get("SKIP_NETWORK") == "1":
        print(f"{len(vistos)} projects checked (GitHub existence check skipped)")
    else:
        resumen = ""
        if nuevos:
            problemas, resumen = revisar_en_github({original[k] for k in nuevos})
            errores += problemas
        print(f"{len(vistos)} projects, {len(nuevos)} new or changed github_id checked on GitHub{resumen}")
    for e in errores:
        print(f"::error file={ruta}::{e}")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
