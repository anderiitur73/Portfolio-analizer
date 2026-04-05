from data_loader import get_data
from metrics import daily_returns,cumulative_returns,volatility,sharpe_ratio,max_drawdown
from plotter import plot_cumulative,plot_drawdown,plot_volatility

tickers = ["SPY", "AAPL", "MSFT"]
data = get_data(tickers)
returns=daily_returns(data)
cum_ret=cumulative_returns(returns)

print(data.head())      # primeras 5 filas
print(data.shape)       # cuántas filas × columnas tienes
print(data.dtypes)      # tipo de dato de cada columna

print("=== Acumulated rent (last five days) ===")
print(cum_ret.tail())

print("\n=== Anual volatility ===")
print(volatility(returns).round(4))

print("\n=== Sharpe Ratio ===")
print(sharpe_ratio(returns).round(4))

print("\n=== Max Drawdown ===")
print(max_drawdown(cum_ret).round(4))

plot_cumulative(cum_ret)
plot_drawdown(cum_ret)
plot_volatility(returns)