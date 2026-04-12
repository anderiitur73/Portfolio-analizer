# Portfolio-analizer
My first code related with the finance world, the aim of this project is given some stocks + their weight, evaluate them with some basic tools.

I created a python tool to calculate some key finantial metrics from real market data. Where you can also generate different plots and compare  the performance of your personal portfolio to SP500, or other standard portfolios (Ex: MSCI_WORLD,NASQD100,EURO50,IBEX35...).

## Features

- Downloads real historical price data via `yfinance`
- Calculates key financial metrics:
  - Daily and cumulative returns
  - Annualized volatility
  - Sharpe Ratio
  - Sortino Ratio
  - Beta vs market
  - Max Drawdown
  - Correlation matrix
- Generates visualizations:
  - Cumulative returns chart
  - Historical drawdown chart
  - Volatility comparison
  - Correlation heatmap
- Compares portfolio performance against S&P 500 with interpretive output

## Project Structure
portfolio-analyzer/
│
├── data/
├── src/
│   ├── main.py          # Entry point — runs the analysis
│   ├── data_loader.py   # Downloads historical price data
│   ├── metrics.py       # Financial metrics calculations
│   └── plotter.py       # Chart generation
|   └── mi_cartera.py    # Practical example with bought stocks
│
├── README.md
└── requirements.txt


## Usage

Edit the tickers and weights in `src/main.py` or `src/mi_cartera.py`:

```python
tickers = ["SPY", "AAPL", "MSFT"]
weights = np.array([0.50, 0.25, 0.25])  # must sum to 1.0
```

Then run:

```bash
python3 src/main.py
```

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- yfinance


## What I learned

- Working with real financial data using `yfinance` and `pandas`
- Implementing key quantitative finance metrics from scratch
- Understanding risk-adjusted returns (Sharpe, Sortino)
- Portfolio construction with weighted assets
- Correlation analysis for diversification assessment
- Data visualization with `matplotlib` and `seaborn`
