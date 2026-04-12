import numpy as np
from data_loader import get_data
from metrics import (daily_returns, cumulative_returns, volatility,
                    sharpe_ratio, max_drawdown, portfolio_returns,
                    sortino_ratio, beta_ratio, correlation_matrix,
                    interpret_portfolio)
from plotter import plot_cumulative, plot_drawdown, plot_correlation,plot_volatility


tickers = [
    "SXRT.DE", "SC0J.DE", "IUSE.L",   # Plan Clásico
    "VVSM.DE", "LOCK.L", "2B76.DE",   # Plan Tecnológico
    "ASML.AS", "NVDA", "EGLN.L",      # Operaciones
    "ISLN.L", "VBTC.DE", "APLD",
    "HAL", "SLB", "VLO"
]

weights = np.array([
    0.1686, 0.2249, 0.1686,   # Plan Clásico
    0.1188, 0.0518, 0.0453,   # Plan Tecnológico
    0.0580, 0.0367, 0.0250,   # Operaciones
    0.0381, 0.0191, 0.0152,
    0.0138, 0.0115, 0.0046
])

print(f"Suma de pesos: {weights.sum():.4f}")  # debe ser ~1.0

data = get_data(tickers, start="2025-09-01")
returns = daily_returns(data)
cum_ret = cumulative_returns(returns)

port_ret = portfolio_returns(returns, weights)
port_cum = cumulative_returns(port_ret)
port_cum.name = "Mi Cartera"

print("\n=== Mi Cartera — Métricas ===")
print(f"Rentabilidad acumulada: {(port_cum.iloc[-1]-1):.2%}")
print(f"Sharpe:       {sharpe_ratio(port_ret):.4f}")
print(f"Sortino:      {sortino_ratio(port_ret):.4f}")
print(f"Volatilidad:  {volatility(port_ret):.2%}")
print(f"Max Drawdown: {max_drawdown(port_cum):.2%}")

print("\n=== Correlación entre activos ===")
print(correlation_matrix(returns))

# Comparación vs SPY
spy_data = get_data(["SPY"], start="2025-09-01")
spy_returns = daily_returns(spy_data)
spy_cum = cumulative_returns(spy_returns.squeeze())

print("\n=== vs S&P 500 ===")
print(interpret_portfolio(port_ret, spy_returns.squeeze(), port_cum, spy_cum))

# Añadir SPY a la comparativa
cum_comparativa = cum_ret.copy()
cum_comparativa["Mi Cartera"] = port_cum
cum_comparativa["SPY"] = spy_cum

plot_cumulative(cum_comparativa)
plot_drawdown(cum_comparativa)
plot_volatility(returns)
plot_correlation(returns)