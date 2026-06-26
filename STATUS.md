# STATUS

## Fase actual

**Fase 1 COMPLETA** — Scaffold + motor + seed verificado.
**Fase 2 COMPLETA** — Discovery enorme agéntico: 75 → **645 tools** verificadas (+570).
**Fase 3 PENDIENTE (handoff abajo)** — Cierre de marca: nombre final, repo remoto público + push, arranque de lista de popularidad + Emergence Picks.

## Estado del repo

- Local: `~/best-of-markets-intelligence`, git inicializado. **NO** hay remoto aún (esperando OK de Arturo para crear repo público — acción irreversible).
- `projects.yaml`: **645 tools** verificadas en 10 categorías (fuente de verdad).
- `README.md`: regenerado E2E (2989 líneas), sincronizado con el yaml. Header/footer/teaser Emergence Picks intactos.
- `_discovery/fase2-report.md`: reporte de provenance del barrido (nuevas por categoría + 223 descartes con motivo).
- Workflow semanal listo (no corre hasta haber remoto).

## Evolution Log

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
