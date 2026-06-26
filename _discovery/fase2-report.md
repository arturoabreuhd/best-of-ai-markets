# Fase 2 — Reporte de Discovery (best-of markets & world intelligence)

Barrido exhaustivo agéntico de GitHub (Workflow multi-agente, 98 agentes, 3.34M tokens, 565 tool-calls, ~34 min).

**Resultado:** 75 → 645 herramientas verificadas (+570). Loop-until-dry: 3 rondas (333 → 163 → 74 nuevas/ronda; nunca llegó a seco — queda cola de cola-larga).

## Nuevas por categoría

| Categoría | Antes | Nuevas | Total |
|---|---|---|---|
| crypto-trading | 14 | +72 | 86 |
| backtesting-quant | 12 | +95 | 107 |
| market-exchange-data | 7 | +102 | 109 |
| defi-tokenomics *(emerging — no inflado)* | 6 | +11 | 17 |
| onchain-analytics *(prioridad Fase 2)* | 2 | +46 | 48 |
| fundamentals-filings | 7 | +30 | 37 |
| macro-geopolitics *(emerging — no inflado)* | 4 | +32 | 36 |
| ai-agents-skills | 10 | +127 | 137 |
| dashboards-data | 5 | +23 | 28 |
| research-discovery | 8 | +32 | 40 |
| **TOTAL** | **75** | **+570** | **645** |

## Verificación aplicada (reglas duras)

Cada candidato superviviente pasó `gh repo view`: existe · ≥20★ · no archivado · `pushedAt ≥ 2024-12-26` (activo ≤18 meses) · encaje genuino en UNA sola categoría. Sin colisiones con los 75 existentes, sin duplicados de `github_id` ni de nombre.

## Descartados (223 candidatos frescos rechazados — nada truncado en silencio)

| Motivo | N |
|---|---|
| inactive(>18mo) | 192 |
| stars<20 | 22 |
| off-domain | 5 |
| archived | 3 |
| not-found | 1 |

### Detalle completo de descartes

<details><summary><b>inactive(>18mo)</b> (192)</summary>

- `0b01/tectonicdb` — Last pushed 2024-01-25, before the 2024-12-26 freshness cutoff. Stale/abandoned.
- `0xaaiden/smoldata` — Inactive since 2023-07, before 2024-12-26 cutoff. Stale.
- `1Hive/conviction-voting-cadcad` — Stale: last push 2020-11. Just a notebook link/redirect repo, abandoned.
- `4gh/WorldBankData.jl` — Stale: last pushed 2023-12-28, well before the 2024-12-26 threshold.
- `51bitquant/multi_pairs_martingle_bot` — pushedAt 2023-12-26 is before the 2024-12-26 cutoff (inactive).
- `AI4Finance-Foundation/FinML` — Stale: last push 2024-02-27, before the 2024-12-26 cutoff. Inactive ML notebook collection.
- `AbdelStark/token-vesting-contracts` — Stale: last push 2024-12-17, just before the 2024-12-26 cutoff. ERC20 vesting contracts but no recent activity.
- `AlainDaccache/Quantropy` — Stale: last pushed 2024-08-20, before the 2024-12-26 cutoff.
- `AlgoTraders/stock-analysis-engine` — Dead: last push 2020-09-05, far before the 2024-12-26 cutoff. Relies on disabled APIs (Yahoo). Stale.
- `AminHP/gym-mtsim` — Stale: last push 2024-11-14, before the 2024-12-26 activity cutoff.
- `BitcoinExchangeFH/BitcoinExchangeFH` — Stale: last push 2023-11-02, well before 2024-12-26 cutoff.
- `CoinQuanta/awesome-crypto-api` — Stale: last pushed 2019-05-10, far below the 2024-12-26 recency threshold. Abandoned list.
- `CryptoGnome/LickHunterPRO` — Stale: last pushed 2022-11-23, well before the 2024-12-26 activity cutoff.
- `CyberPunkMetalHead/Binance-News-Sentiment-Bot` — Fails recency gate: last pushed 2022-03-16, far before 2024-12-26 cutoff. Stale/unmaintained.
- `CyberPunkMetalHead/backtesting-for-cryptocurrency-trading` — Last push 2021-06 — inactive, below 2024-12-26 threshold.
- `CyberPunkMetalHead/gateio-crypto-trading-bot-binance-announcements-new-coins` — Stale: last pushed 2022-02, far before 2024-12-26 cutoff.
- `Elenchev/order-book-heatmap` — Last pushed 2021-03-09, far before cutoff. Author labels it a short exploratory project; inactive.
- `Erfaniaa/binance-futures-trading-bot` — pushedAt 2024-03-13 is well before the 2024-12-26 cutoff (stale).
- `Erfaniaa/crypto-trading-strategy-backtester` — Last pushed 2023-09-26, before the 2024-12-26 cutoff. Inactive.
- `ExchangeUnion/market-maker-bot` — Stale: last pushed 2023-01-06, before cutoff.
- `FRBNY-TimeSeriesAnalysis/Nowcasting` — Stale: last push 2019-09-26, far before cutoff. MATLAB nowcasting toolbox is on-domain but abandoned.
- `FinancialDataGirl/awesome-fintech` — Stale: last pushed 2018-12, far before cutoff.
- `Indian-Algorithmic-Trading-Community/PythonTraderExcelTradeTerminal` — Last push 2024-08-17, before the 2024-12-26 freshness cutoff. Stale.
- `JumpCrypto/crypto-reading-list` — Stale: last push 2024-08-06, before the 2024-12-26 cutoff.
- `L4ventures/awesome-cryptoeconomics` — Dead: last push 2018-07, abandoned ~8 years; far below freshness cutoff.
- `PSLmodels/CGE` — Stale: last pushed 2024-07-17, before the 2024-12-26 freshness cutoff.
- `PierreRochard/coinbase-exchange-order-book` — Last pushed 2021-01-28, far before the 2024-12-26 freshness cutoff. Dead repo (targets deprecated GDAX API).
- `PyWaves/BlackBot` — Stale: last pushed 2021-02, far before cutoff.
- `Rleahy22/fredApi` — Stale: last pushed 2021-08-07, well before the 2024-12-26 activity threshold.
- `SpiralDevelopment/Awesome-Crypto-Trading` — Stale: last push 2020-07-30, before cutoff.
- `StephanAkkerman/crypto-ohlcv` — Last push 2023-08-09, well before the 2024-12-26 cutoff. Stale; also references defunct FTX.
- `TheAIQuant/StockScreener_Streamlit` — Stale: last push 2024-08-20, before the 2024-12-26 freshness cutoff.
- `Theling/10-K-scraper` — Last push 2018; abandoned single-purpose script far past cutoff.
- `TiesdeKok/fast_xbrl_parser` — Last push 2023-09, inactive (before cutoff).
- `TokenEngineeringCommunity/BalancerPools_Model` — Stale: last push 2021-12-14, far below the 2024-12-26 activity cutoff. Abandoned cadCAD Balancer AMM model.
- `TokenEngineeringCommunity/resources` — Stale: last push 2024-04-10, below the 2024-12-26 cutoff. Curated TE resource list but not maintained.
- `TulipCharts/tulipy` — Last push 2021-07, explicitly NOT actively maintained — far below 2024-12-26 activity threshold.
- `VivekPa/OptimalPortfolio` — Stale: last push 2024-02-27, before the 2024-12-26 activity cutoff.
- `WISEPLAT/backtrader_binance` — Last push 2024-09-30, before the 2024-12-26 cutoff.
- `Xtra-Computing/CryptoTrade` — pushedAt 2024-12-01 is before the 2024-12-26 freshness cutoff; stale research-paper repo (EMNLP 2024), no longer maintained.
- `Yeachan-Heo/Certis` — Last push 2022-10-13, far before the 2024-12-26 cutoff. Inactive.
- `Yvictor/TradingGym` — Last push 2024-02-11, before the 2024-12-26 cutoff.
- `aamend/spark-gdelt` — Stale: last push 2023-04-21, before cutoff.
- `aarigs/pandas-ta` — Last push 2019-03 — dead fork, below activity threshold.
- `adyzng/go-duka` — Last pushed 2018; long abandoned (< 2024-12-26 cutoff). Fails recency requirement.
- `amv-dev/yata` — Last push 2024-09-19, before the 2024-12-26 freshness cutoff. Legit Rust TA library but stale.
- `analyseether/ether_sql` — Python lib to push Ethereum data into SQL but last pushed 2022-09-13, far before cutoff (stale/abandoned).
- `anandanand84/technicalindicators` — Stale: last push 2022-11-03, before cutoff. Unmaintained.
- `antontarasenko/awesome-economics` — Stale: last pushed 2023-08-26, well before the 2024-12-26 freshness cutoff.
- `bergant/XBRLFiles` — Last push 2015, dead (before cutoff). Also a demo/explore repo, not a library.
- `bergant/finstr` — Last push 2017, long inactive (well before 2024-12-26 cutoff).
- `bergant/xbrlus` — Last push 2018, inactive (before cutoff).
- `blockchain-etl/awesome-bigquery-views` — Stale: last push 2022-11-06, years before the cutoff.
- `blockchain-etl/bitcoin-etl-airflow` — Inactive since 2022-04 (last push >4y ago, before 2024-12-26 cutoff). Stale.
- `blockchain-etl/blockchain-etl-streaming` — Stale: last push 2021-12-09, years before the cutoff.
- `blockchain-etl/polygon-etl` — Polygon ETL to BigQuery but last pushed 2024-09-10, before the 2024-12-26 cutoff (stale).
- `blockchain-etl/public-datasets` — Stale: last push 2024-06-26, before the 2024-12-26 cutoff.
- `blockchain-unica/blockapi` — Stale: last push 2022-01-15, years before the cutoff.
- `bmoscon/cryptostore` — Pushed 2024-04-18, before the 2024-12-26 cutoff. Otherwise a legitimate crypto market-data storage service, but fails freshness.
- `boudra/chainsauce` — Last push 2024-08-20, before 2024-12-26 cutoff. Stale.
- `bradleyboyuyang/ML-HFT` — Last pushed 2022-09-20, far before the 2024-12-26 freshness cutoff. Inactive.
- `bseddon/XBRL` — Last push 2021-12, inactive (before 2024-12-26 cutoff).
- `cadCAD-org/cadcad-ri` — Stale: last push 2023-12-29, below the 2024-12-26 cutoff.
- `calcbench/python_api_client` — Last push 2024-12-10 falls just before the 2024-12-26 freshness cutoff. Drop on recency.
- `carlos8f/bot18` — pushedAt 2022-12-02 is far before cutoff (inactive).
- `codesociety/friartuck` — Last push 2023-01-13, well before the 2024-12-26 staleness cutoff. Dead/inactive.
- `colekennelly1/awesome-defi-trackers` — Stale: last push 2022-06-04, before cutoff.
- `commons-stack/commons-simulator` — Stale: last push 2023-01, below activity cutoff. Abandoned cadCAD Commons simulator.
- `conor19w/Binance-Futures-Trading-Bot` — Stale: last pushed 2024-07, before the 2024-12-26 freshness cutoff.
- `cyber-drop/ethereum_analytical_db` — Ethereum ClickHouse analytics DB but last pushed 2022-07-13, far before cutoff (stale/abandoned).
- `czielinski/portfolioopt` — Stale: last push 2022-08, before the 2024-12-26 cutoff. Inactive portfolio optimization library.
- `danielsobrado/edgar-cik-cusip-ticker-sector-service` — Last push 2023-04-09, before the 2024-12-26 cutoff. Stale.
- `danpaquin/coinbasepro-python` — Stale: last push 2023-07 (before 2024-12-26 cutoff); also targets deprecated Coinbase Pro API.
- `davidkellis/stocktrader_clojure` — Inactive since 2010 — far below the 2024-12-26 freshness cutoff.
- `dcSpark/carp` — Modular Cardano indexer but last pushed 2024-10-01, before the 2024-12-26 freshness cutoff (stale).
- `deepeth/mars` — Stale: last push 2023-06, before the 2024-12-26 freshness cutoff.
- `devfinwiz/Stock_Screeners_Raw` — Stale: last push 2023-09-14, before the 2024-12-26 cutoff. Inactive.
- `doug2k1/my-money` — Stale: last push 2023-01-24, far before the 2024-12-26 cutoff.
- `dpc/rust-bitcoin-indexer` — Stale: last push 2022-09-14, far before 2024-12-26 cutoff.
- `dr-leo/pandaSDMX` — Stale: last push 2023-12-28, before 2024-12-26 cutoff. Otherwise relevant SDMX interface.
- `edgarminers/filingsdb` — Last push 2020-10, long inactive (before cutoff).
- `elsaifym/EDGAR-Parsing` — Last push 2021; stale, below freshness cutoff.
- `enzoampil/fastquant` — Inactive: last push 2023-09-15, well before the 2024-12-26 activity cutoff. Domain fits but fails freshness.
- `farhadab/sec-edgar-financials` — Stale: last push 2023-05-22, well before the 2024-12-26 activity cutoff. Effectively unmaintained.
- `fastquant/fastquant.dll` — Inactive since 2016 — below freshness cutoff.
- `featherenvy/botvana` — pushedAt 2022-05-12 is far before cutoff (abandoned, early development).
- `femtotrader/pandas_talib` — Last push 2018-05 — dead, below activity threshold.
- `foolcage/fooltrader` — Stale: last push 2023-05-22, before cutoff. Quant framework but inactive.
- `fortesenselabs/trade_flow` — Last pushed 2024-12-05, which is before the 2024-12-26 activity cutoff.
- `fremantle-industries/tai` — pushedAt 2024-12-07 is before the 2024-12-26 freshness cutoff (inactive).
- `fyangch/crypto-dashboard` — Stale: last push 2023-06-29, well before the 2024-12-26 cutoff.
- `gazbert/bxbot` — Stale: last pushed 2024-11-30, just before the 2024-12-26 cutoff.
- `gdelt/gdelt.github.io` — Stale: last push 2023-11-30, before cutoff.
- `getamis/eth-indexer` — Stale: last push 2022-12-14, far before 2024-12-26 cutoff. Abandoned indexer.
- `gshs-ornl/wbstats` — Stale: last push 2023-12-02, before cutoff. R World Bank package, otherwise relevant.
- `guanquann/Stocksera` — Last pushed 2024-08-19, before the 2024-12-26 cutoff. Relevant alt-data dashboard but stale.
- `hadialaddin/crypto-genie` — Stale: last pushed 2023-07-31, before cutoff.
- `hello2all/gamma-ray` — Last pushed 2022-02-07, before the 2024-12-26 cutoff. Inactive.
- `hjones20/fundamental-analysis` — Stale: last push 2020-06-11, far before the 2024-12-26 activity cutoff. Effectively abandoned.
- `hrbrmstr/newsflash` — Stale: last push 2022-12-01, well before cutoff.
- `hrshtsharma17/Stock-SEC-Data-Dashboard` — Last pushed 2023-09-08 — fails freshness gate (pushedAt < 2024-12-26). Inactive ETL project.
- `hudson-and-thames/mlfinlab` — Inactive: last push 2023-10-02, well before 2024-12-26 cutoff (repo went closed-source).
- `hudson-and-thames/portfoliolab` — Stale: last pushed 2021-12-02, far before the 2024-12-26 freshness cutoff.
- `hylinux1024/awesome-blockchain-articles` — Stale: last push 2019-11-13, before cutoff. Also a learning-articles collection (tutorial-like).
- `ibigquant/awesome-trading-api` — Stale: last push 2019-03-10, far before cutoff.
- `idanya/algo-trader` — Stale: last pushed 2023-11, before the 2024-12-26 freshness cutoff.
- `imanoop7/Financial-Analysis--Multi-Agent-Open-Source-LLM` — pushedAt 2024-11-20 is before the 2024-12-26 freshness cutoff; inactive >1.5y. Also no description/topics, reads as a tutorial-style demo repo.
- `indexooor/indexooor-stack` — Last push 2023-03-26, far before the 2024-12-26 freshness cutoff. Abandoned.
- `ivopetiz/crypto-database` — Last pushed 2019-10-04, far before cutoff. Dead project.
- `jadchaar/sec-edgar-api` — Stale: last push 2024-07-10, before the 2024-12-26 activity cutoff.
- `jankrepl/deepdow` — Inactive: last push 2024-01-24, before the 2024-12-26 cutoff. Domain fits but fails freshness.
- `javagg/freequant` — Abandoned since 2013 — far below freshness cutoff.
- `jcrichard/pyrb` — Stale: last pushed 2023-07-06, before the 2024-12-26 cutoff.
- `jkbrzt/cointrol` — Fails recency gate: last pushed 2023-08-26, before 2024-12-26 cutoff. Bitstamp-only legacy bot.
- `joelowj/awesome-algorithmic-trading` — Last pushed 2019-05-21, well below freshness cutoff. Curated list is stale/unmaintained.
- `josephchenhk/qtrader` — Stale: last push 2024-02-23, before the 2024-12-26 activity cutoff.
- `junhua/awesome-finance-ai-papers` — Stale: last pushed 2024-11-24, before the 2024-12-26 cutoff.
- `just-nilux/awesome-tradingview` — Stale: last push 2023-05-02, before the 2024-12-26 cutoff.
- `karlwancl/Trady` — Last pushed 2021 — stale, below the freshness cutoff.
- `kruglov-dmitry/crypto_crawler` — Last pushed 2019-09-17, far below the 2024-12-26 freshness cutoff. Python 2.7 arbitrage bot, abandoned.
- `kungfu-origin/kungfu` — Last push 2024-05-02, before the 2024-12-26 freshness cutoff. Otherwise a legit low-latency quant system.
- `lequant40/portfolio_allocation_js` — Stale: last pushed 2023-03-03, before the 2024-12-26 cutoff.
- `letianzj/QuantResearch` — Stale: last push 2023-08-26, before cutoff. Also a notebook collection rather than maintained tool.
- `letianzj/quanttrader` — Stale: last push 2024-06-20, before the 2024-12-26 activity cutoff.
- `litaotao/Awesome-FinTech` — Stale: last pushed 2019-06-05, far older than the 2024-12-26 cutoff. Abandoned awesome-list.
- `llamafolio/evm-indexer` — Stale: last push 2023-04, before the 2024-12-26 freshness cutoff.
- `lukstei/trading-backtest` — Last pushed 2021-07-20, below freshness cutoff. Java backtest engine, unmaintained.
- `m12t/bsm-time-machine` — Last pushed 2023-10-07, before the 2024-12-26 cutoff. Inactive.
- `maanavshah/stock-market-india` — Stale: last push 2023-12-17, before 2024-12-26 cutoff.
- `maihde/quant` — Last pushed 2015-08-31, a decade stale. Abandoned.
- `manifoldfinance/awesome-ethereum-finance` — Stale: last push 2022-04-25, well before the 2024-12-26 freshness cutoff. Curated Ethereum-finance list fits research-discovery but is abandoned.
- `manu354/cryptocurrency-arbitrage` — Stale: last pushed 2022-05, well before the 2024-12-26 freshness cutoff.
- `marcioalexandre/XbrlParser` — Last push 2024-06-20, before the 2024-12-26 freshness cutoff. Stale.
- `markusaksli/TradeBot` — Stale: last pushed 2024-11-05, just before 2024-12-26 cutoff.
- `matplotlib/mplfinance` — Last pushed 2024-08-08, before the 2024-12-26 cutoff. Popular and relevant but fails freshness rule.
- `mementum/bta-lib` — Inactive since Jan 2022 (>4 years stale, well before 2024-12-26 cutoff). pandas TA library but abandoned.
- `mempool/mempool-cli` — Last push 2023-03-27, before the 2024-12-26 cutoff. Stale.
- `mikeroyal/Blockchain-Guide` — Stale: last push 2022-04-28, far before the 2024-12-26 cutoff. Awesome-list blockchain guide is on-domain but unmaintained.
- `mikispag/bitiodine` — Stale: last push 2022-11-17, years before the cutoff.
- `mmssss/hft-market-making` — Stale: last push 2023-05, before cutoff.
- `mohdabdin/crypto-trading-RL-environment` — Stale: last pushed 2021-03-13, far before the 2024-12-26 freshness cutoff.
- `mwaldstein/edgarWebR` — Last push 2022-06-02, far older than the 2024-12-26 cutoff. Stale R package.
- `nelso0/barbotine-scalping-bot` — pushedAt 2024-07-06 is before the 2024-12-26 cutoff (stale).
- `neo4j-examples/sec-edgar-notebooks` — Stale: last pushed 2024-04-23, before the 2024-12-26 activity cutoff. Also a WIP experiment/notebook collection rather than a maintained tool.
- `nkaz001/gridtrading` — Last pushed 2022 — stale, below the 2024-12-26 cutoff.
- `nkaz001/market-making-backtest` — Stale: last push 2023-12, before cutoff.
- `nvincenthill/Nicks-Bloomberg-Terminal` — Stale: last pushed 2021-08, well before 2024-12-26 cutoff. Also a personal Yahoo/Bloomberg knockoff toy project.
- `opensanctions/offshore-graph` — Stale: last pushed 2024-12-17, 9 days before the 2024-12-26 threshold.
- `orshe4/marketstack` — Last pushed 2021-03; stale (< 2024-12-26 cutoff). Fails recency requirement.
- `patelneel55/financialmodelingprep` — Stale: last pushed 2023-04-12, well before the 2024-12-26 cutoff. Unmaintained.
- `pegahcarter/TAcharts` — Last pushed 2023-01-01, well before the cutoff. Inactive.
- `penberg/helix` — Last pushed 2017-10-18, long before the 2024-12-26 cutoff. Inactive.
- `petercerno/trader-backtest` — Last push 2023-02-19, before the 2024-12-26 cutoff. Inactive.
- `pipiku915/FinMem-LLM-StockTrading` — Last push 2024-08-18, before the 2024-12-26 recency cutoff; stale/inactive.
- `piquette/edgr` — Last push 2019-11-18, far older than the 2024-12-26 activity cutoff. Inactive/stale.
- `prmkowalski/filib` — Last pushed 2022-11-12, before the 2024-12-26 cutoff. Inactive.
- `purefinance/mmb` — Stale: last push 2022-11-17, well before 2024-12-26 cutoff. Otherwise a fit (Rust market-making bot).
- `qmhedging/poboquant` — Last pushed 2020-01-20, below freshness cutoff. Abandoned.
- `quantopian/alphalens` — Inactive: last push 2024-02-12, before 2024-12-26 cutoff (Quantopian defunct).
- `quantopian/zipline` — Inactive: last push 2024-02-13, before the 2024-12-26 freshness cutoff. Repo is effectively abandoned (Quantopian defunct).
- `rchardzhu/awesome-quant-cn` — Stale: last pushed 2022-06, well before cutoff.
- `rorysroes/SGX-Full-OrderBook-Tick-Data-Trading-Strategy` — Stale: last push 2022-08, far before cutoff; also a notebook strategy demo rather than a maintained tool.
- `rsljr/edgarParser` — Stale: last push 2023-02-27 (Jupyter notebooks), far before the 2024-12-26 cutoff.
- `s915/DBnomics.jl` — Stale: last push 2022-07-17, well before cutoff.
- `sadighian/crypto-rl` — Stale: last push 2022-01, far before cutoff.
- `sanzol-tech/ai-trader` — Stale: last pushed 2023-02-13, before cutoff.
- `secdatabase/SEC-XBRL-Financial-Statement-Dataset` — Last push 2021-11-14, well before the 2024-12-26 cutoff. Stale dataset.
- `second-state/smart-contract-search-engine` — Dead: last push 2020-09, well before the 2024-12-26 freshness cutoff.
- `shirosaidev/stocksight` — Stale: last push 2023-12-05, before cutoff. Sentiment-based stock analyzer but inactive.
- `shobrook/BitVision` — Stale: last push 2022-12-08, before cutoff. Inactive terminal Bitcoin trading/forecasting tool.
- `simonschoe/scraper-edgar` — Last push 2023-12-24, before the 2024-12-26 cutoff. Stale.
- `smzerehpoush/binance-spot-trading-bot` — Stale: last pushed 2022-08-02, before cutoff.
- `spacecodewor/fmpcloud-go` — Stale: last pushed 2024-07-23, before the 2024-12-26 cutoff.
- `spidezad/yahoo_finance_data_extract` — Abandoned since 2016; loose collection of scripts rather than a maintained library. Far below freshness cutoff.
- `stevenpack/cryptowarrior` — Dead: last push 2017-11, abandoned for ~9 years; far below freshness cutoff.
- `thetruetrade/gotrade` — Abandoned since 2014 (>10 years stale). Far below freshness cutoff.
- `thrasher-corp/gct-ta` — Last pushed 2021-05; stale (< 2024-12-26 cutoff). Fails recency requirement.
- `tiansin/docker_grid_trader` — Stale: last pushed 2021-05-05, far before cutoff.
- `tooksoi/ScraXBRL` — Last push 2022-12-26, far older than the 2024-12-26 freshness cutoff. Inactive.
- `tradytics/eiten` — Stale: last push 2022-07-30, well before 2024-12-26 cutoff. Abandoned.
- `tsaol/Web3-serverless-analytics-on-aws` — AWS Ethereum analytics pipeline but last pushed 2023-10-05, far before cutoff; reference/demo project (stale).
- `tzuhsial/edgar-10k-mda` — Last push 2024-09-17, before the 2024-12-26 cutoff. Stale.
- `unageanu/jiji2` — Stale: last push 2021-04, before the 2024-12-26 cutoff. Inactive forex trading framework.
- `universal-exchange/awesome-trading-system` — Stale: last push 2020-05-10, before cutoff.
- `we-commit/in-dex-explorer` — Last push 2022-12-17, long before the cutoff. Abandoned.
- `webn3ewbie/OpenBBxStreamlit` — Fails recency: last push 2023-06-28, well before the 2024-12-26 cutoff (inactive ~3 years). Otherwise a relevant OpenBB+Streamlit dashboard, but stale.
- `wynfred/presso` — Last pushed 2021-10-19, well before the 2024-12-26 cutoff. Inactive.
- `xFFFFF/Gekko-Strategies` — Stale: last push 2020-01-09, well before 2024-12-26 cutoff. Strategies for the defunct Gekko bot.
- `yahoo-finance/yahoo-finance` — Last pushed 2023-12-25 — one year before the freshness cutoff; abandoned.
- `yearn/yearn-vesting-escrow` — Stale: last push 2024-03-28, before cutoff. Token vesting escrow but inactive.
- `yungwine/ton-mempool` — Last push 2024-04-26, before the 2024-12-26 freshness cutoff. Stale.
- `zbarge/stocklook` — Stale: last push 2018-06, well before the 2024-12-26 cutoff. Abandoned crypto library.

</details>

<details><summary><b>stars<20</b> (22)</summary>

- `Adamant-im/ETH-transactions-storage` — Stale: last push 2024-02-13, before the 2024-12-26 freshness cutoff. Drop despite 575 stars.
- `AlgoTrader5/cryptoq` — Last push 2021-04 — inactive, below activity threshold despite 24 stars.
- `CADLabs/ethereum-economic-model` — 139 stars and on-topic (Ethereum validator economics model) but last push 2024-08-14 — before the 2024-12-26 activity threshold.
- `Corfucinas/crypto-candlesticks` — Last push 2024-11-18, before the 2024-12-26 cutoff. Stale despite 43 stars and on-domain candlestick download tool.
- `Crypto-toolbox/HFT-Orderbook` — Last push 2024-11-13, before the 2024-12-26 cutoff. Popular (1376 stars) and on-domain limit-order-book lib, but stale by the freshness rule.
- `MajesticKhan/Nowcasting-Python` — Stale: last push 2021-02-07, well before the 2024-12-26 activity cutoff (no maintenance in ~5 years) despite 133 stars and relevant DFM nowcasting domain.
- `The-Swarm-Corporation/awesome-financial-agents` — Stale: last push 2024-10-16, before the 2024-12-26 cutoff. Meets stars (20) and fits research-discovery as a curated list of AI financial agents, but fails freshness.
- `alexey-ernest/go-hft-orderbook` — Last push 2023-12-18, before the 2024-12-26 cutoff. Stale despite 277 stars and on-domain Go limit order book.
- `alpha-miner/Finance-Python` — Last pushed 2024-01-01, before the 2024-12-26 cutoff. Stale despite 900 stars.
- `cadCAD-org/cadCAD` — 614 stars and on-topic (tokenomics/complex-systems simulation) but last push 2024-04-19 — before the 2024-12-26 activity threshold.
- `epogrebnyak/weo-reader` — Stale: last push 2024-07-09, before the 2024-12-26 activity cutoff. Otherwise a legitimate IMF WEO macro-data client with 41 stars.
- `euclidjda/deep-quant` — Last pushed 2019-07-23 — fails freshness gate (pushedAt < 2024-12-26). Dead/abandoned despite 141 stars.
- `gauss314/defi` — Strong fit and 606 stars, but last push 2024-03-02 is before the 2024-12-26 freshness cutoff. Stale.
- `joeyism/py-edgar` — Last push 2024-10-13, before the 2024-12-26 cutoff despite strong stars. Stale.
- `jpantunes/awesome-cryptoeconomics` — Stale: last push 2024-06-17, before the 2024-12-26 cutoff despite 1772 stars.
- `linwoodc3/gdeltPyR` — Last push 2023-11; 253 stars but stale, below freshness cutoff.
- `passabilities/crypto-exchange` — Last push 2018-07-21, abandoned for ~8 years (far before cutoff). High stars but dead; references defunct exchanges (gdax, btc-e, yunbi).
- `portfedh/fundamental_analysis_report` — Single personal Jupyter notebook script to generate one analysis report, not a reusable tool/library/framework. Reads as a toy/personal project despite meeting 20-star and activity thresholds.
- `starknet-io/tokei` — Stale: last push 2024-01-30, before cutoff. Starknet token streaming protocol but inactive.
- `toddwschneider/sec-13f-filings` — Strong repo (423 stars) but last push 2024-08-01, before 2024-12-26 cutoff. Stale.
- `valamidev/candlestick-convert` — Last push 2024-10-14, before the 2024-12-26 freshness cutoff. Stars (55) and domain are fine but it is stale.
- `warp-id/solana-trading-bot` — Stale: last pushed 2024-08-10, before 2024-12-26 cutoff despite 2330 stars.

</details>

<details><summary><b>off-domain</b> (5)</summary>

- `SoYuCry/awesome-quant-interview` — Active and 417 stars, but it is a quant-finance interview/study guide (course-style prep material), not a markets tool nor a curated list of tools. Off-domain for a tools best-of.
- `brycewang-stanford/Awesome-Journal-Skills` — Academic-publishing skill packs for journals across all fields (Nature, Cell, AER); a paper-writing assistant, not a markets/finance-intelligence tool. Out of domain.
- `ignaciohermosillacornejo/copilot-money-mcp` — MCP server for the Copilot Money personal-budgeting app (personal-finance/expense tracking), not a markets/trading/crypto/macro/finance-AI tool. Off-domain for this list.
- `jackson-video-resources/claude-tradingview-mcp-trading` — Owner org 'jackson-video-resources' and bare repo (no topics, thin) indicate a YouTube/video-tutorial companion demo rather than a maintained standalone tool. Fails the 'not a tutorial/toy' fit criterion despite 538 stars.
- `robcerda/monarch-mcp-server` — MCP server for Monarch Money, a personal budgeting / net-worth tracking app. 257 stars, active, but off-domain: personal-finance management, not markets/trading/crypto/macro intelligence. Does not genuinely fit any category in the list.

</details>

<details><summary><b>archived</b> (3)</summary>

- `constverum/Quantdom` — Stale: last push 2022-07-06, well before the 2024-12-26 freshness cutoff. Otherwise a legit backtesting framework (771 stars, not archived).
- `greyblake/ta-rs` — Stale: last push 2024-07-12, before the 2024-12-26 freshness cutoff. Otherwise a legit Rust TA library (863 stars, not archived).
- `seanlion/Awesome-Defi-Study-Resource` — Stale: last push 2022-05-02, before cutoff. Also a study/presentation archive, thin domain fit.

</details>

<details><summary><b>not-found</b> (1)</summary>

- `nexus-trade-bot/nexus-trade-bot` — Repository does not exist (gh resolved to no repository).

</details>
