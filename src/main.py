import numpy as np
from data_loader import get_data
from metrics import daily_returns,cumulative_returns,volatility,sharpe_ratio,max_drawdown,portfolio_returns,sortino_ratio
from plotter import plot_cumulative,plot_drawdown,plot_volatility

tickers = ["SPY", "AAPL", "MSFT"]
data = get_data(tickers)
returns=daily_returns(data)
cum_ret=cumulative_returns(returns)

weights = np.array([0.50, 0.25, 0.25])  # SPY, AAPL, MSFT

port_ret = portfolio_returns(returns, weights)
port_cum = cumulative_returns(port_ret)
port_cum.name = "Portfolio" 


cum_comparativa = cum_ret.copy()
cum_comparativa["Portfolio"] = port_cum

print("=== Individual asset metrics ===")
print(f"Sharpe:  {sharpe_ratio(returns).round(4)}")
print(f"Sortino: {sortino_ratio(returns).round(4)}")

print("=== Portfolio metrics ===")
print(f"Sharpe:      {sharpe_ratio(port_ret):.4f}")
print(f"Sortino:     {sortino_ratio(port_ret):.4f}")
print(f"Volatility: {volatility(port_ret):.4f}")
print(f"Max Drawdown:{max_drawdown(port_cum):.4f}")
print(f"Acumulated rent: {port_cum.iloc[-1]:.4f}")

"""
plot_cumulative(cum_comparativa)
plot_drawdown(cum_comparativa)
plot_volatility(returns)
"""