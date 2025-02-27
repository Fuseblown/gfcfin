# GFC Financial

Didn't know what else to call it. Open to suggestions.

## Project Description

Automate backtesting and trading of various market trading strategies for financial gain. In time, we would essentially be creating a private hedge fund between the project's contributors and whomever we determine and agree upon beyond that. Open to discussion and suggestions for longer-term and end goals.

## Primary Goals

- Obtain preliminary backtesting results for various mechanical trading strategies

## Usage Instructions

Clone the repository and change to the new directory:

```bash
git clone https://github.com/Fuseblown/gfcfin.git

cd gfcfin
```

Setup your favorite development environment. I personally use Conda and Python 3.9:

```bash
conda create -n gfcfin python=3.9
```

Activate the environment:

```bash
conda activate gfcfin
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run `main.py`. The first time executing this file will download sample data (~392MB) from Google Drive and save it to the `'./data'` directory.

```bash
python main.py
```

By default, the `LiquidityReversalSniper()` strategy class is run and currently outputs the following in the terminal:

```bash
Setup Timeframe Analysis:
                              price                               swing_high swing_low
                               Open      High       Low     Close
Date
2023-11-30 19:00:00-05:00  15964.25  15964.25  15958.25  15963.25      False     False
2023-11-30 19:15:00-05:00  15962.75  15963.75  15959.50  15961.50      False     False
2023-11-30 19:30:00-05:00  15961.25  15961.25  15956.75  15959.50      False     False
2023-11-30 19:45:00-05:00  15959.75  15959.75  15955.00  15958.75      False     False
2023-11-30 20:00:00-05:00  15958.75  15962.25  15953.50  15954.25      False     False
2023-11-30 20:15:00-05:00  15954.50  15958.50  15951.25  15955.75       True     False
2023-11-30 20:30:00-05:00  15955.50  15961.00  15954.00  15958.00      False      True
2023-11-30 20:45:00-05:00  15958.25  15962.75  15952.50  15953.50      False     False
2023-11-30 21:00:00-05:00  15953.50  15958.25  15952.00  15955.00       True     False
2023-11-30 21:15:00-05:00  15955.25  15959.75  15954.25  15959.50      False      True
...                             ...       ...       ...       ...        ...       ...
2023-12-15 07:00:00-05:00  16596.25  16599.75  16593.50  16594.25      False     False
2023-12-15 07:15:00-05:00  16595.00  16602.25  16595.00  16599.75      False      True
2023-12-15 07:30:00-05:00  16599.50  16602.75  16595.00  16595.00      False     False
2023-12-15 07:45:00-05:00  16595.25  16596.75  16584.00  16586.25       True     False
2023-12-15 08:00:00-05:00  16588.50  16592.50  16584.00  16590.00      False     False
2023-12-15 08:15:00-05:00  16592.00  16595.25  16584.00  16595.25      False     False
2023-12-15 08:30:00-05:00  16596.75  16603.50  16549.25  16567.75      False     False
2023-12-15 08:45:00-05:00  16565.25  16580.00  16560.50  16580.00       True      True
2023-12-15 09:00:00-05:00  16584.00  16601.00  16576.75  16598.75      False     False
2023-12-15 09:15:00-05:00  16598.75  16612.50  16521.50  16558.00      False     False

[1402 rows x 6 columns]

Strategy Signals:
Last swing high: 16580.0
Last swing low: 16560.5

Trade Timeframe Data:
                              price                               Volume bullish_fvg bearish_fvg
                               Open      High       Low     Close Volume
Date
2023-11-30 19:00:00-05:00  15964.25  15964.25  15962.25  15963.75     93       False       False
2023-11-30 19:01:00-05:00  15963.50  15963.50  15963.00  15963.25     18       False       False
2023-11-30 19:02:00-05:00  15962.75  15962.75  15960.25  15960.25     67       False       False
2023-11-30 19:03:00-05:00  15960.25  15961.25  15959.50  15960.00     64       False        True
2023-11-30 19:04:00-05:00  15960.00  15960.00  15958.25  15959.00     61       False        True
2023-11-30 19:05:00-05:00  15959.00  15961.00  15959.00  15960.75     42       False       False
2023-11-30 19:06:00-05:00  15960.75  15961.75  15960.25  15961.25     50        True       False
2023-11-30 19:07:00-05:00  15962.00  15963.00  15961.50  15962.75     87        True       False
2023-11-30 19:08:00-05:00  15962.50  15962.50  15961.75  15962.25     33       False       False
2023-11-30 19:09:00-05:00  15962.25  15963.00  15962.25  15962.75     17       False       False
...                             ...       ...       ...       ...    ...         ...         ...
2023-12-15 09:20:00-05:00  16605.50  16607.00  16603.75  16604.25     62       False       False
2023-12-15 09:21:00-05:00  16604.25  16609.75  16604.00  16607.25     35       False       False
2023-12-15 09:22:00-05:00  16606.00  16607.00  16603.75  16603.75     50       False       False
2023-12-15 09:23:00-05:00  16603.75  16604.00  16598.75  16600.25     49       False       False
2023-12-15 09:24:00-05:00  16601.00  16607.75  16599.00  16601.25     33       False       False
2023-12-15 09:25:00-05:00  16600.75  16602.25  16595.00  16595.50     58       False       False
2023-12-15 09:26:00-05:00  16595.75  16602.25  16579.00  16584.50     48       False       False
2023-12-15 09:27:00-05:00  16588.00  16597.00  16575.00  16580.50     25       False       False
2023-12-15 09:28:00-05:00  16580.50  16589.00  16544.75  16559.25     54       False       False
2023-12-15 09:29:00-05:00  16552.50  16582.00  16521.50  16558.00     79       False       False

[21030 rows x 7 columns]
```

## NASDAQ Index Futures Test Data

The primary instruments that will be traded are the NASDAQ Index Futures e-Mini and Micro e-Mini contracts (Base symbol: NQ and MNQ, respectively) Most of my strategies are based on this instrument alone, although will work in most cases across all markets and timeframes because price is fractal and delivered by an algorithm.

There are many reasons for trading index futures, commodity futures, options, etc., but the primary reasons for me are due to the leverage provided, tax benefits, liquidity, and efficient price delivery. Most third-party funding companies also provide access to index futures and similar instruments and we will leverage those companies, especially early on, because there are many added benefits such as very low capital risk and additional tax benefits.

### Granular Data

Trade (or tick) data in CSV format from DataBento.io is structured like the following:

```plaintext

ts_recv,ts_event,rtype,publisher_id,instrument_id,action,side,depth,price,size,flags,ts_in_delta,sequence,symbol
2023-12-01 00:00:00.003574803+00:00,2023-12-01 00:00:00.003140441+00:00,0,1,260937,T,A,0,15964.25,1,0,15774,177919674,NQZ3
2023-12-01 00:00:00.517622404+00:00,2023-12-01 00:00:00.517401231+00:00,0,1,260937,T,B,0,15964.25,1,0,16315,177920136,NQZ3
2023-12-01 00:00:00.793528846+00:00,2023-12-01 00:00:00.793302653+00:00,0,1,260937,T,A,0,15963.75,1,0,16472,177920265,NQZ3
2023-12-01 00:00:00.793974319+00:00,2023-12-01 00:00:00.793741049+00:00,0,1,260937,T,B,0,15963.75,1,0,16385,177920279,NQZ3
2023-12-01 00:00:00.794359802+00:00,2023-12-01 00:00:00.794139967+00:00,0,1,260937,T,A,0,15963.75,1,0,15912,177920296,NQZ3
2023-12-01 00:00:00.794764403+00:00,2023-12-01 00:00:00.794556273+00:00,0,1,260937,T,B,0,15963.75,1,0,16017,177920308,NQZ3
2023-12-01 00:00:00.794845276+00:00,2023-12-01 00:00:00.794661091+00:00,0,1,260937,T,B,0,15963.75,1,0,13544,177920310,NQZ3
2023-12-01 00:00:00.795109214+00:00,2023-12-01 00:00:00.794893847+00:00,0,1,260937,T,A,0,15963.75,1,0,15683,177920323,NQZ3
2023-12-01 00:00:00.859256386+00:00,2023-12-01 00:00:00.859046341+00:00,0,1,260937,T,B,0,15963.75,1,0,15701,177920416,NQZ3
2023-12-01 00:00:01.176491213+00:00,2023-12-01 00:00:01.176271205+00:00,0,1,260937,T,A,0,15963.5,1,0,15944,177920718,NQZ3
```

All of the examples orders above except for the last transpired within the first second after midnight UTC on 2023-12-01. This is the most granular data provided and is used to simulate the most accurate trade executions. However, in most cases, it will be aggregated into "Open, High, Low, Close" data points for filtering and identifying trade setups.

**NEW as of 12/14/2024!** When running main.py successfully for the first time, following the Usage Instructions, the sample data from the Google Drive link below will be automatically downloaded and saved in the `'./data'` directory.

You can find an unabridged copy of the DataBento CSV source data from shown above to use for development and testing at: <https://drive.google.com/file/d/1WE4YTNmtWPSvEsYBDD_V2lUYEE_J_sMJ/view?usp=sharing>

#### Aggregated Data

1-minute aggregated OHLC data using the granular data from above will look like this:

```plaintext
datetime,open,high,low,close
2023-11-30 19:00:00-05:00,15964.25,15964.25,15962.25,15963.75
2023-11-30 19:01:00-05:00,15963.5,15963.5,15963.0,15963.25
2023-11-30 19:02:00-05:00,15962.75,15962.75,15960.25,15960.25
2023-11-30 19:03:00-05:00,15960.25,15961.25,15959.5,15960.0
2023-11-30 19:04:00-05:00,15960.0,15960.0,15958.25,15959.0
2023-11-30 19:05:00-05:00,15959.0,15961.0,15959.0,15960.75
2023-11-30 19:06:00-05:00,15960.75,15961.75,15960.25,15961.25
2023-11-30 19:07:00-05:00,15962.0,15963.0,15961.5,15962.75
2023-11-30 19:08:00-05:00,15962.5,15962.5,15961.75,15962.25
2023-11-30 19:09:00-05:00,15962.25,15963.0,15962.25,15962.75
2023-11-30 19:10:00-05:00,15962.75,15963.5,15962.75,15963.25
```

This OHLC data is the underlying information that forms the bodies and wicks of candles on a candlestick chart. Utilizing reoccuring, mechanical and algorithmic patterns within these candles are how we print money.

## Random Thoughts

- Utilizing the Jesse trading bot project (<https://jesse.trade> and <https://github.com/jesse-ai/jesse>) would allow for testing and trading cryptocurrencies
  - Jesse could be forked and customized to import the data we need for futures, forex, stocks, options, etc.
    - Could be our own standalone project or could contribute to the main project
    - Could still make our own thing from scratch using Python or C++ or whatever makes the most sense
  - Could be a shortcut to a creating a more robust platform without "reinventing the wheel"
  - Need to successfully code one of our strategies on the Jesse platform before deciding how to move ahead with it

---

## Backtest System Architecture

```mermaid
flowchart TB
    subgraph main[main.py]
        direction TB
        M1[Initialize Strategy] --> M2[Fetch Data]
        M2 --> M3[Run Analysis]
        M3 --> M4[Get Signals]
        M4 --> M5[Display Results]
    end

    subgraph dh[data_handler.py]
        direction TB
        D1[fetch_data] --> D2[Download from GDrive]
        D2 --> D3[Process CSV Data]
        D3 --> D4[Resample Timeframes]
    end

    subgraph strat[strategies.py]
        direction TB
        subgraph ls[LiquidityReversalSniper]
            L1[Initialize] --> L2[Set Timeframes]
            L2 --> L3[Analyze Data]
            L3 --> L4[Get Signals]
        end
    end

    subgraph pat[patterns.py]
        direction TB
        P1[detect_swing_points]
        P2[get_last_swing_points]
        P3[detect_fair_value_gaps]
        P4[get_last_fair_value_gaps]
    end

    subgraph util[utils.py]
        U1[debug_df]
    end

    M1 --> L1
    M2 --> D1
    D4 --> L3
    L3 --> P1
    L3 --> P2
    L3 --> P3
    L3 --> P4
    M5 --> U1

    classDef primary fill:#f9f,stroke:#333,stroke-width:2px;
    classDef secondary fill:#bbf,stroke:#333,stroke-width:1px;
    classDef utility fill:#ddd,stroke:#333,stroke-width:1px;

    class main,strat primary;
    class dh,pat secondary;
    class util utility;
```

---

## CFTC RISK DISCLAIMER

### Trading involves risk

All financial trading involves significant risk.

### You are solely responsible for all trading profit or loss

Only you are responsible for the trades you take, including trades taken through automated trading systems you may in any manner employ.

You alone are ultimately and completely responsible for all testing and quality assurance of all trading systems, methods and technologies you may employ, and you alone bear the full profit or loss of any and all trading activities you may undertake.

### Risk of trading futures, options, equities, and forex

There is a significant risk of loss in futures, forex, equities, and options trading - including trades taken online. Trade only with capital you can afford to lose. Past performance in not necessarily indicative of future results. Nothing within this repository or codebase or that we may separately convey is intended to be a recommendation to buy or sell any market or instrument. All information has been obtained from sources and methods which are believed to be reliable, but accuracy and thoroughness cannot be guaranteed. You alone are solely responsible for how to use the information and for the results. We do not guarantee the accuracy or completeness of any information or any analysis based thereon.

### Hypothetical performance

Hypothetical performance results have many inherent limitations, some of which are described below. No representation is being made that any account will or is likely to achieve profits or losses similar to those shown. In fact, there are frequently sharp differences between hypothetical performance results and the actual results subsequently achieved by any particular trading program.

One of the limitations of hypothetical performance results is that they are generally prepared with the benefit of hindsight. In addition, hypothetical trading does not involve financial risk, and no hypothetical trading record can completely account for the impact of financial risk in actual trading. For example, the ability to withstand losses or to adhere to a particular trading program in spite of trading losses are material points which can also adversely affect actual trading results. There are numerous other factors related to the markets in general or to the implementation of any specific trading program which cannot be fully accounted for in the preparation of hypothetical performance results and all of which can adversely affect actual trading results.

We do not trade actual accounts for clients. Because there are no actual trading results to compare to any hypothetical performance results to in advance of live trading, clients should be particularly wary of placing undue reliance on hypothetical performance results.

Commission Rule 4.41(c)(1) applies to "any publication, distribution or broadcast of any report, letter, circular, memorandum, publication, writing, advertisement or other literature…." Commission Rule 4.41(b) prohibits any person from presenting the performance of any simulated or hypothetical futures account or futures interest of a CTA, unless the presentation is accompanied by a disclosure statement. The statement describes the limitations of simulated or hypothetical futures trading as a guide to the performance that a CTA is likely to achieve in actual trading.

### Additional risk disclosure for systems traders

Commission Rule 4.41(b)(1)(I) hypothetical or simulated performance results have certain inherent limitations. Unlike an actual performance record, simulated results do not represent actual trading. Also, since the trades have not actually been executed, the results may have under-compensated or over-compensated for the impact, if any, of certain market factors, such as lack of liquidity. Simulated trading programs in general are also subject to the fact that they are designed with the benefit of hindsight. No representation is being made that any account will or is likely to achieve profits or losses. There have been no promises, guarantees or warranties suggesting that any trading will result in a profit or will not result in a loss.
