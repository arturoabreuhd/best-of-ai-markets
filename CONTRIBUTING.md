# Contributing

This list is **generated** from [`projects.yaml`](./projects.yaml). Never edit `README.md` by hand — it is overwritten weekly by the [best-of generator](https://github.com/best-of-lists/best-of-generator).

## Add or update a tool

1. Edit `projects.yaml`.
2. Add an entry under `projects:` with at least:
   ```yaml
   - name: My Tool
     github_id: owner/repo
     category: crypto-trading   # must match a category id below
     labels: ["mcp"]            # optional
   ```
3. Open a pull request. An automatic check validates it (known category and labels, no duplicates, the repo exists, is not archived and uses its current name). The weekly job regenerates the README after merge.

Not comfortable with pull requests? [Suggest a tool](https://github.com/arturoabreuhd/best-of-ai-markets/issues/new?template=suggest-tool.yml) with an issue instead.

### Category ids

`crypto-trading` · `backtesting-quant` · `market-exchange-data` · `defi-tokenomics` · `onchain-analytics` · `fundamentals-filings` · `macro-geopolitics` · `ai-agents-skills` · `dashboards-data` · `research-discovery`

### Labels

`mcp` · `skill` · `awesome` · `ai-native` · `self-hosted`

## Inclusion bar

A tool is judged on open-source merit, activity, and usefulness — not stars alone. Genuinely useful low-star tools in sparse domains (tokenomics, geopolitical risk) are welcome and clearly framed as emerging.

## Emergence Picks

To nominate a tool for the hand-curated, epistemically-vetted shortlist, label your PR `emergence-candidate` and explain *why* in the description (what it does better, what it's verified against).

## Regenerating locally (maintainers)

`best-of` 0.8.5 has not been maintained since 2022, and GitHub now rejects one field of its query
(`stargazers { totalCount }`), which leaves every project without data. The weekly workflow applies a
one-field patch; do the same locally:

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install best-of==0.8.5
python .github/scripts/parche_best_of.py
export GITHUB_API_KEY=$(gh auth token)
best-of generate projects.yaml
```
