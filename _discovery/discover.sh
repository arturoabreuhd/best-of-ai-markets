#!/usr/bin/env bash
# Discovery feeder for best-of-markets-intelligence.
# Sweeps GitHub by topic + keyword, dedups against projects.yaml, and prints
# candidate repos NOT yet in the list, ranked by stars. Review, then add to projects.yaml.
#
# Usage:  ./discover.sh            # run all category sweeps
#         ./discover.sh "<query>"  # run one ad-hoc query
#
# Requires: gh (authenticated), python3.11
set -euo pipefail
cd "$(dirname "$0")/.."

YAML="projects.yaml"
LIMIT=20

# Collect github_ids already in the list (lowercased) to dedup against.
existing=$(grep -oE 'github_id: *[^ ]+' "$YAML" | sed -E 's/github_id: *//' | tr '[:upper:]' '[:lower:]' | sort -u)

emit() {
  # $1 = label, $2.. = gh search args
  local label="$1"; shift
  echo "### $label"
  gh search repos "$@" --sort stars --order desc --limit "$LIMIT" \
    --json fullName,stargazersCount,description,updatedAt 2>/dev/null \
  | EXISTING="$existing" python3.11 -c '
import json, os, sys
existing = set(os.environ["EXISTING"].split("\n"))
for r in json.load(sys.stdin):
    fid = r["fullName"].lower()
    if fid in existing:
        continue
    desc = (r.get("description") or "")[:62]
    print(f"  {r[\"stargazersCount\"]:>7}* {r[\"updatedAt\"][:7]} | {r[\"fullName\"]:<46} | {desc}")
'
  echo
}

if [ "$#" -ge 1 ]; then
  emit "ad-hoc: $1" "$1"
  exit 0
fi

# --- category sweeps (extend freely) ---
emit "crypto-trading"        --topic=trading-bot --topic=cryptocurrency
emit "backtesting"           --topic=backtesting
emit "quant"                 --topic=quantitative-finance
emit "algotrading"           --topic=algorithmic-trading
emit "market-data"           "crypto exchange api"
emit "defi"                  --topic=defi --topic=analytics
emit "tokenomics"            "token unlock vesting analysis"
emit "onchain"               "on-chain analytics ethereum solana"
emit "sec-edgar"             "sec edgar filings python"
emit "geopolitics"           "geopolitical risk intelligence"
emit "macro"                 "macroeconomic data api"
emit "mcp-servers"           --topic=mcp-server
emit "agent-skills"          --topic=claude-skills
emit "ai-finance"            "LLM agent trading finance"

echo "Done. Candidates above are NOT yet in $YAML. Add the good ones, then regenerate."
