# best-of markets & world intelligence — Project Tesis

## Qué es

Una lista pública **best-of** (ranked, auto-mantenida) de herramientas open-source para leer mercados y el mundo con IA: crypto, trading, tokenomics, macro, geopolítica, y los agentes/skills/MCP que los conectan. Hecha con [`best-of-generator`](https://github.com/best-of-lists/best-of-generator).

## Por qué (posicionamiento de marca Emergence)

Es la **capa de alcance** de una estrategia de dos listas:

1. **Esta (el mar)** — exhaustiva, cientos de herramientas, taxonomía clara, *todo donde veamos valor*. Su trabajo es traer tráfico/stars y ser encontrada. Diferenciador honesto: **descubierta por metadata Y por código** (no se le escapan tools sin topic) y **re-puntuada cada semana** (nunca se pudre, a diferencia de las awesome-lists hechas a mano).
2. **Emergence Picks (el moat)** — repo/sección aparte, hand-curada con metodología y epistemología de Arturo (procedencia, falla ruidosa, etiqueta de confianza ley/regularidad/marco/metáfora). NO existe aún; esta lista enlaza a ella como embudo.

La marca de Emergence es *"rigor anti-humo"*. El producto no es ninguna lista: es **el método visible de pasar de cientos a unas pocas**.

## Principios duros

- **Verificar antes de añadir.** Ningún `github_id` entra al yaml sin confirmar que existe (`gh repo view`). No inventar repos.
- **Honestidad de dominio.** Tokenomics y geopolítica son dominios delgados (pocas tools con tracción real). Se marcan como *emerging / best-available*, NO se inflan.
- **El README es generado.** Nunca editar `README.md` a mano; la fuente de verdad es `projects.yaml`.
- **Salud visible.** El score de calidad y los flags (💤 inactivo, 💀 muerto) son el rigor hecho visible. No esconderlos.
- **min_stars: 20** — deja entrar nichos legítimos pequeños, excluye ruido.

## Stack

- `projects.yaml` → fuente de verdad (github_id + category + labels).
- `best-of-generator` (pip `best-of`) → genera README. Regen local: `export GITHUB_API_KEY=$(gh auth token); best-of generate projects.yaml` (~3-4 min, 1 llamada API/proyecto).
- `.github/workflows/update-best-of-list.yml` → refresh semanal (jueves 14h UTC), abre PR + draft release. Endurecido contra inyección.
- `_discovery/discover.sh` → feeder: barre GitHub, deduplica contra yaml, imprime candidatos nuevos.

## Categorías (10)

`crypto-trading` · `backtesting-quant` · `market-exchange-data` · `defi-tokenomics` · `onchain-analytics` · `fundamentals-filings` · `macro-geopolitics` · `ai-agents-skills` · `dashboards-data` · `research-discovery`

## Capa de descubrimiento (herramientas verificadas vivas jun-2026)

- **gh search repos** (CLI, base, 5000 req/h; search 30/min) — caballo de batalla.
- **ecosyste.ms** — API abierta sin key, metadata + dependientes. Mejor feeder gratis.
- **Sourcegraph** — búsqueda por *contenido de código* (lo que el topic pierde).
- **OSS Insight** — trending (feeder de la futura lista de popularidad).
- **SEART GitHub Search**, **GH Archive/BigQuery** — barridos académicos / historia de estrellas (opcional, después).
