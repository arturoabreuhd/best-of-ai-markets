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
3. Open a pull request. The weekly job (or a maintainer running it) regenerates the README.

### Category ids

`crypto-trading` · `backtesting-quant` · `market-exchange-data` · `defi-tokenomics` · `onchain-analytics` · `fundamentals-filings` · `macro-geopolitics` · `ai-agents-skills` · `dashboards-data` · `research-discovery`

### Labels

`mcp` · `skill` · `awesome` · `ai-native` · `self-hosted`

## Inclusion bar

A tool is judged on open-source merit, activity, and usefulness — not stars alone. Genuinely useful low-star tools in sparse domains (tokenomics, geopolitical risk) are welcome and clearly framed as emerging.

## Emergence Picks

To nominate a tool for the hand-curated, epistemically-vetted shortlist, label your PR `emergence-candidate` and explain *why* in the description (what it does better, what it's verified against).

## Regenerating locally (maintainers)

```bash
pip install best-of
export GITHUB_API_KEY=$(gh auth token)
best-of generate projects.yaml
```
