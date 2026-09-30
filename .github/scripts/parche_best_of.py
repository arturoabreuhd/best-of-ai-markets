"""Parche para best-of 0.8.5 (sin mantenimiento desde 2022).

Desde 2026 GitHub responde FORBIDDEN al campo GraphQL `stargazers { totalCount }`
con tokens de integración, y la consulta entera vuelve con `repository: null`:
el README sale sin estrellas, licencias ni enlaces. `stargazerCount` sí se permite.
Falla en voz alta si el código instalado no es el esperado.
"""
import pathlib
import sys

import best_of.integrations.github_integration as m

ruta = pathlib.Path(m.__file__)
codigo = ruta.read_text()
cambios = [
    ("    stargazers {\n      totalCount\n    }\n", "    stargazerCount\n"),
    (
        "    if github_info.stargazers and github_info.stargazers.totalCount:\n"
        "        star_count = int(github_info.stargazers.totalCount)\n",
        "    if github_info.stargazerCount:\n"
        "        star_count = int(github_info.stargazerCount)\n",
    ),
]
for viejo, nuevo in cambios:
    if codigo.count(viejo) != 1:
        sys.exit(f"parche_best_of: no encontré exactamente una vez:\n{viejo}")
    codigo = codigo.replace(viejo, nuevo)
ruta.write_text(codigo)
print(f"parche_best_of: {len(cambios)} cambios aplicados en {ruta}")
