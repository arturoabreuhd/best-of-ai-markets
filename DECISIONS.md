# DECISIONS

> Cada decisión no trivial: qué, por qué, evidencia, alternativas, qué la invalidaría. Nunca borrar; marcar superseded.

## D1 — Modelo de dos listas (mar + curada), no una
- **Qué:** Lista grande exhaustiva auto-mantenida + lista curada aparte (Emergence Picks).
- **Por qué:** La grande da alcance/SEO; la curada da el moat de marca. El contraste ("escaneamos cientos, ponemos el nombre en pocas") ES el pitch. Separarlas en dos repos perdería el contraste → van conectadas, la curada cuelga de la grande.
- **Alternativa descartada:** una sola lista curada (poca tracción) o un solo mar maximalista (commodity, compite contra hubs de 19k stars y pierde, y contradice "rigor anti-humo").
- **Invalidaría:** si la audiencia no convierte del mar a la marca.

## D2 — best-of-generator como motor (no awesome-list a mano)
- **Qué:** Generar el README desde `projects.yaml` con best-of-generator + Action semanal.
- **Por qué:** Una lista grande a mano se pudre y una lista podrida bajo "rigor" hunde la marca. El motor re-puntúa salud semanalmente → la automatización ES parte del rigor visible.
- **Evidencia:** best-of-generator vivo (ago-2025); best-of-ml-python auto-actualiza en 2026; generación probada E2E local.
- **Riesgo aceptado:** update-action wrapper estancado desde 2022. Mitigación: pin de versión, forkeable (80 líneas).

## D3 — Nicho: "markets & world intelligence", no "best-of-todo"
- **Qué:** Crypto/trading/tokenomics/macro/geo/AI-tools, no una lista genérica.
- **Por qué:** Listas genéricas compiten contra awesome-lists gigantes y se pierden. Un nicho claro se puede poseer ("LA lista de X"). Coincide con audiencia y marca de Arturo.
- **Invalidaría:** si los 11k seguidores resultan ser de otro vertical (asunción de Arturo, confirmada).

## D4 — min_stars: 20, sin filtro de licencia
- **Qué:** Umbral 20★; no restringir por licencia.
- **Por qué:** Deja entrar nichos legítimos (token-vesting 22★, geopolrisk-py 18★) y excluye spam; no dropear tools por metadata de licencia faltante (común en repos crypto).
- **Alternativa:** 300 (best-of-ml-python) mataría tokenomics/geo enteras.

## D5 — Honestidad de dominios delgados
- **Qué:** Tokenomics y geopolítica marcadas explícitamente "emerging / best-available".
- **Por qué:** El topic `tokenomics` es ~spam de un autor; pocas tools reales. Inflar contradice la marca. Mejor declarar el hueco.

## D6 — Discovery agéntico para Fase 2 (Workflow)
- **Qué:** Barrido enorme vía Workflow multi-agente (fan-out por categoría×modalidad, dedup, loop-until-dry, verify, append, regen).
- **Por qué:** Arturo autorizó gasto alto para exhaustividad; es fan-out independiente clásico. Modalidades múltiples (topic + keyword + ecosyste.ms + Sourcegraph) cubren lo que una sola búsqueda pierde.

## D7 — Adiciones research-driven + exclusiones por honestidad de dominio (Fase 2c/2d/2e)
- **Qué:** +23 tools (657→680) vía cross-check con Grok + barrido org-by-org. Excluidos pese a stars enormes: sherlock (85k★, OSINT username), spiderfoot (19k★, threat-intel), modelcontextprotocol/* (87k★, infra MCP genérica), foundry-rs/foundry (10k★, dev-toolkit Solidity), paradigmxyz/reth (5.6k★, nodo Ethereum), langchain/langgraph (35k★, framework agentes genérico).
- **Por qué:** La marca es "anti-humo": cada entrada debe SER lo que dice. Tools que no leen mercados/mundo (OSINT de personas, infra de protocolo, nodos, dev-frameworks) diluyen justo el diferenciador. Meter 100k+ estrellas daría tráfico pero rompería la promesa de dominio.
- **Invalidaría:** si decidimos que la lista es "todo AI tooling" en vez de "leer mercados/mundo con IA" — entonces MCP SDKs y agent frameworks entrarían. Hoy el scope es el dominio, no la forma.
- **Evidencia del valor:** Grok nunca inventó nombres (0 fantasmas en 4 rondas) pero sí sobrevende relevancia/métricas — exactamente el ruido que la lista filtra con verificación `gh repo view`.

## D8 — Regla de asignación dominio×forma (reorg pre-launch)
- **Qué:** Un tool va a su categoría de **DOMINIO** (crypto-trading, onchain-analytics, macro-geopolitics, etc.); `mcp`/`skill`/`ai-native` son SIEMPRE labels, nunca el criterio de categoría. `ai-agents-skills` queda SOLO para frameworks de agentes sin dominio propio (genéricos). Ej.: un MCP de datos on-chain → onchain-analytics [mcp], NO ai-agents-skills.
- **Por qué:** Hoy "agentes/skills/MCP" está doble-codificado (categoría ai-agents-skills=149 + labels mcp/skill). Eso crea ambigüedad: un MCP de trading puede caer en crypto-trading[mcp] o ai-agents-skills[mcp]. Fijar la regla vuelve el cruce dominio×forma predecible para un LLM que busca "un MCP para X".
- **Alcance:** mueve ~80-100 entradas de ai-agents-skills hacia sus dominios. Solo yaml, reversible, no toca verificación. Hacer ANTES de promocionar; regenerar README después.
- **Invalidaría:** si los usuarios buscan primero por forma ("dame todos los MCP") más que por dominio — entonces ai-agents-skills como hub tendría sentido. Apuesta: buscan por dominio + filtran por label.
