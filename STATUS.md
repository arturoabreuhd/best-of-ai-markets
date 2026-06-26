# STATUS

## Fase actual

**Fase 1 COMPLETA** — Scaffold + motor + seed verificado (75 → 73 tras recategorizar).
**Fase 2 PENDIENTE (handoff abajo)** — Discovery enorme agéntico para llevar el mar a 300-600+ tools.

## Estado del repo

- Local: `~/best-of-markets-intelligence`, git inicializado, 1 commit. **NO** hay remoto aún (esperando OK de Arturo para crear repo público — acción irreversible).
- `projects.yaml`: ~73 tools verificadas en 10 categorías.
- `README.md`: generado y probado E2E. **OJO: está desincronizado** tras los 3 movimientos de recategorización del cierre de Fase 1 → **primera acción de Fase 2 = regenerar.**
- Workflow semanal listo (no corre hasta haber remoto).

## Evolution Log

- **2026-06-26 — Fase 1.** Investigación de tooling (best-of-generator confirmado vivo ago-2025; update-action estancado 2022 pero funcional, listas insignia auto-actualizan en 2026). Capa de discovery mapeada y verificada viva (gh, ecosyste.ms, Sourcegraph, OSS Insight, SEART). Scaffold creado, seed de 75 tools verificadas vía `gh`, README generado E2E (543 líneas), workflow endurecido contra inyección (lo cazó un hook). Recategorización: peregrine + crypto-arbitrage-framework → crypto-trading; DeFiHackLabs → research-discovery. `onchain-analytics` quedó delgada (2 tools) — Fase 2 debe llenarla.

---

## HANDOFF — Fase 2: Discovery enorme (correr en contexto limpio)

**Objetivo:** barrer exhaustivamente GitHub y llevar `projects.yaml` de ~73 a 300-600+ tools verificadas, bien categorizadas, sin duplicados, sin repos muertos/archivados. Arturo autorizó gastar lo necesario ("barrer absolutamente todo").

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
