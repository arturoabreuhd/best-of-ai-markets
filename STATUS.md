# STATUS

## Fase actual

**Fase 1 COMPLETA** — Scaffold + motor + seed verificado.
**Fase 2 COMPLETA** — Discovery: 75 → **680 tools** verificadas (barrido agéntico +570 → 645, luego research-driven Grok cross-check + org-by-org → 680).
**REORG pre-launch D8 COMPLETO** — 90 MOVE · 58 STAY. `ai-agents-skills` 148→58; las demás categorías absorbieron los connectors/MCPs/skills a su dominio + label de forma. Solo yaml. Falta regen README vía `!` antes de publicar.
**Fase 3 EN CURSO** — Repo público + push HECHO (2026-06-26). Falta: toggle PRs de Actions (Arturo), lista de popularidad (OSS Insight) + Emergence Picks (moat hand-curado).

## Estado del repo

- **PÚBLICO 2026-06-26**: `https://github.com/arturoabreuhd/best-of-ai-markets` (HEAD `67feded`, 680 tools, taxonomía D8). Local: `~/best-of-markets-intelligence`, remote `origin` → ese repo. ⚠️ Falta que Arturo active "Allow GitHub Actions to create and approve PRs" (Settings → Actions → General) o el PR semanal del jueves no se abre (la rama update + draft release sí).
- `projects.yaml`: **680 tools** verificadas en 10 categorías (fuente de verdad).
- `README.md`: resync en curso (task background) para reflejar las 680. Header/footer/teaser Emergence Picks intactos. Se regenerará otra vez tras el reorg D8.
- `_discovery/fase2-report.md`: reporte de provenance del barrido (nuevas por categoría + 223 descartes con motivo).
- Workflow semanal listo (no corre hasta haber remoto).

## Evolution Log

- **2026-06-26 — Reorg D8 (dominio×forma).** Disuelto el cajón de sastre `ai-agents-skills` (148): clasificación delegada a subagente (ventana limpia, rationale por entrada → `_discovery/d8-reclassification.tsv`), auditada, aplicada con script determinista. **90 MOVE · 58 STAY.** ai-agents-skills 148→58 (solo quedan frameworks/runtimes de agentes genéricos y skill-packs multi-dominio). Connectors/MCPs/SDKs/skill-packs atados a una fuente concreta fueron a su dominio + label de forma: market-exchange-data 117→151, backtesting-quant 113→121, crypto-trading 87→95, onchain-analytics 53→61, research-discovery 44→52, fundamentals-filings 38→45, defi-tokenomics 19→28, macro-geopolitics 38. Las 148 no tenían labels; 147 ahora llevan label de forma. Validado: 680 proyectos, 0 categorías/labels inválidos. Motivación: findability — un MCP on-chain enterrado en "ai-agents-skills" no aparecía al buscar "on-chain". README pendiente de regen (`!` o CI). Ver D8 EJECUTADO.

- **2026-06-26 — Fase 2e (sub-repos flagship).** Grok cross-check org-por-org: confirmó que todos los flagships ya estaban (Lean, nautilus_trader, freqtrade, hummingbot, jesse, vnpy, qlib, gs-quant, OpenBB, ccxt, FinGPT/FinRL, dtale, ArcticDB, StockSharp, blankly). **6 sub-repos nuevos añadidos:** nautilus_agents (ai-agents), FreqUI (dashboards), hummingbot/quants-lab (backtesting), hummingbot/condor (ai-agents), hummingbot/gateway (market-exchange), owid/owid-grapher (macro-geopolitics, 1.5k★ — engine de Our World in Data). Excluidos: QuantConnect/Research (push may-2024, pasa cutoff 18mo), langchain-ai/langgraph (35k★ — framework de agentes genérico, no finanzas). **674 → 680.** README desincronizado (680 yaml vs 645 generado) — pendiente resync (CI jueves o `!`).

- **2026-06-26 — Fase 2d (org-by-org sweep).** `gh repo list` sobre 9 orgs insignia (gs-quant/goldmansachs, man-group, AI4Finance, OpenBB-finance, paradigmxyz, foundry-rs, duneanalytics, messari, modelcontextprotocol). Método más limpio que keyword: listado por-org (no `search`, no flagged). De ~60 repos `NEW` la mayoría se descartó por **off-domain** (compiladores Solidity de foundry-rs, ORMs Java de goldmansachs, nodos Ethereum/reth, SDKs genéricos de protocolo MCP, dev-wallets) — disciplina de dominio. **12 añadidos:** D-Tale (dashboards), FinRL-X/FinRL-Meta/FinRL_Crypto (backtesting, ai-native), Awesome AI4Finance + Awesome OpenBB (research, awesome), Agents-for-OpenBB + OpenBB AI SDK (ai-agents), Spice + Dune Spellbook + Dune Python Client + Messari Subgraphs (onchain-analytics). **662 → 674.** Excluidos notables por honestidad de dominio pese a stars enormes: modelcontextprotocol/* (87k★ servers — infra genérica MCP, no mercados), foundry-rs/foundry (10k★ — dev toolkit Solidity), paradigmxyz/reth (5.6k★ — nodo Ethereum). FinRL-DeepSeek ya estaba. README desincronizado (674 yaml).

- **2026-06-26 — Fase 2c (perps SDKs, Grok cross-check).** 3 rondas de Grok sobre orderflow/perps/macro-OSINT. De 12 candidatos: 3 ya en yaml (cryptofeed, ccxt, fredapi — Grok no lo sabía, 0 inventados), 1 archivado descartado (Polymarket/py-clob-client), 2 duplicados entre sí (drift-labs/protocol-v2 → velocity-exchange/protocol-v2, mismo repo tras transferencia), 2 off-domain excluidos por honestidad de dominio (smicallef/spiderfoot 19k★ threat-intel, sherlock-project/sherlock 85k★ username-OSINT — ninguno lee mercados/macro). **5 añadidos a market-exchange-data** (perps SDKs verificados vivos): hyperliquid-python-sdk 1688★, velocity-exchange/protocol-v2 398★, dydx v4-clients 119★, paradex-py 33★, vertex-python-sdk 22★ (este 💤, push may-2025, pasa cutoff 18mo). **657 → 662.** Confirmación de tesis: el error de Grok no es inventar nombres (0 ghosts) sino sobrevender relevancia/métricas. README desincronizado (662 yaml vs 645 README) — resync en CI jueves o `!` manual. `gh search` sigue flagged (spammy temporal); `gh repo view` operativo (toda la verificación se hizo con él).

- **2026-06-26 — Fase 2 (discovery enorme).** Workflow multi-agente (98 agentes, 3.34M tokens, 565 tool-calls, ~34 min): loop-until-dry K=2 por categoría × modalidad (gh topic → keyword ES+EN → long-tail/código). 3 rondas (333→163→74 nuevas/ronda; nunca llegó a seco — queda cola-larga). Verificación dura por candidato vía `gh repo view`: existe · ≥20★ · no archivado · `pushedAt ≥ 2024-12-26`. **75 → 645** (+570), 0 dups de id/nombre, cada repo en UNA categoría. **onchain-analytics 2→48** (prioridad cumplida). Emerging respetadas: defi-tokenomics 6→17, macro-geopolitics 4→36 (reales, no infladas). 223 descartes registrados por motivo (190+ inactivos, 22 <20★, 5 off-domain, 3 archivados, 1 inexistente) — 0 truncados en silencio. README regenerado por Arturo vía `!` (el token `gh auth token` está en deny-list de seguridad, no pasa por Claude). Decisiones técnicas: nombres duplicados desambiguados con owner (4 casos); labels filtradas al set válido; bloque appendeado agrupado por categoría al final del yaml (el orden de archivo no afecta la salida — best-of agrupa por campo `category`).
- **2026-06-26 — Fase 1.** Investigación de tooling (best-of-generator confirmado vivo ago-2025; update-action estancado 2022 pero funcional, listas insignia auto-actualizan en 2026). Capa de discovery mapeada y verificada viva (gh, ecosyste.ms, Sourcegraph, OSS Insight, SEART). Scaffold creado, seed de 75 tools verificadas vía `gh`, README generado E2E (543 líneas), workflow endurecido contra inyección (lo cazó un hook). Recategorización: peregrine + crypto-arbitrage-framework → crypto-trading; DeFiHackLabs → research-discovery. `onchain-analytics` quedó delgada (2 tools) — Fase 2 debe llenarla.

---

## HANDOFF — Fase 3: Cierre de marca (pendiente, decisiones de Arturo)

Fase 2 quedó cerrada y commiteada. Lo que falta requiere decisiones de producto / acciones irreversibles:

1. **Nombre final de marca** de la lista (el título actual es "best-of markets & world intelligence").
2. **Crear repo remoto público + push** (irreversible — requiere OK explícito). Al haber remoto, el GitHub Action semanal empieza a correr (jueves 14h UTC).
3. **Arrancar la lista de popularidad** (OSS Insight, feeder ya mapeado) y la **curada Emergence Picks** (el moat hand-curado; hoy solo enlazada como teaser).

Notas para retomar discovery más adelante (la cola-larga NO está agotada): el loop-until-dry nunca llegó a seco en 3 rondas. Reusar el workflow `_discovery` o el script en `~/.claude/.../workflows/scripts/best-of-discovery-*.js` (embeber la lista `EXISTING_IDS` actualizada desde el yaml; `args` no se inyecta — hardcodear). Token: `gh auth token` está en deny-list; el regen del README lo corre Arturo vía `!` o el CI tras el push.

---

## HANDOFF — Fase 2: Discovery enorme (COMPLETADA — histórico)

**Objetivo:** barrer exhaustivamente GitHub y llevar `projects.yaml` de ~73 a 300-600+ tools verificadas, bien categorizadas, sin duplicados, sin repos muertos/archivados. Arturo autorizó gastar lo necesario ("barrer absolutamente todo"). **Resultado: 645 tools.**

### Recomendación: SÍ, flujo agéntico (Workflow)

Es un caso ideal de fan-out: muchas búsquedas independientes + verificación + categorización. Diseño recomendado para el `Workflow`:

**Fase A — Fan-out de descubrimiento (parallel/pipeline).** Una unidad de trabajo por `(categoría × modalidad de búsqueda)`. Modalidades:
- `gh search repos` por topic (lista amplia de topics por categoría)
- `gh search repos` por keyword (sinónimos, ES+EN)
- ecosyste.ms API (sin key) — enriquecimiento + dependientes de los anchors ya listados
- Sourcegraph — búsqueda por contenido de código (ej. "imports ccxt", "mcp server" + finance) para cazar lo que el topic pierde
Cada agente devuelve `[{github_id, stars, pushedAt, archived, desc}]`.

**Fase B — Dedup + filtro (código, no agente).** Unir todo, lowercase, deduplicar contra `projects.yaml` actual y entre sí. Descartar: `archived=true`, `pushedAt` > 18 meses (muerto), `stars < 20`.

**Fase C — Loop-until-dry por categoría.** Repetir A+B con queries variadas hasta que K=2 rondas no traigan repos nuevos sobre umbral. Registrar (log) lo que se descarta — nunca truncar en silencio.

**Fase D — Categorización + verificación (parallel).** Por candidato sobreviviente: confirmar `gh repo view` (existe, stars, no archivado) y asignar la categoría correcta de las 10. Un agente verificador puede revisar lotes.

**Fase E — Append al yaml + regenerar.** Escribir entradas nuevas en `projects.yaml` (mismo formato), luego `export GITHUB_API_KEY=$(gh auth token); best-of generate projects.yaml`. Commit.

### Reglas duras de Fase 2 (del CLAUDE.md)

- Verificar existencia antes de añadir. NUNCA inventar github_id.
- No inflar tokenomics/geopolítica — marcar emerging.
- Cada repo en UNA sola categoría; revisar miscategorización (arbitraje≠onchain, educativo≠analytics).
- Rellenar `onchain-analytics` (hoy solo 2).
- Mantener el header/footer y el teaser de Emergence Picks intactos.

### Notas técnicas

- `gh` autenticado como `arturoabreuhd`. Python 3.11 en `/usr/local/bin/python3.11`; CLI `best-of` en `/Library/Frameworks/Python.framework/Versions/3.11/bin/best-of`.
- Permisos del shell: redirects `>` a archivo y backgrounding `&`/`nohup` a veces son denegados — usar pipes o el flag de background del tool, no `&`.
- `gh repo view` usa `stargazerCount` (sin "s"); `gh search repos --json` usa `stargazersCount` (con "s"). No confundir.
- Generación = ~1 llamada API/proyecto; 300 tools ≈ 15-20 min. Correr con timeout largo o en background.

### Cuando Fase 2 termine

Preguntar a Arturo: (1) nombre final de marca, (2) crear repo remoto público + push, (3) arrancar la lista de **popularidad** (OSS Insight) y la **curada Emergence Picks**.
