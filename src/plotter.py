import matplotlib.pyplot as plt
import seaborn as sns

def plot_cumulative(cum_returns):
    cum_returns.plot(figsize=(12, 6))
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Growth of €1")
    plt.axhline(y=1, color="gray", linestyle="--", linewidth=0.8)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_drawdown(cum_returns):
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    drawdown.plot(figsize=(12, 5))
    plt.title("Historical Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drop from peak")
    plt.axhline(y=0, color="gray", linestyle="--", linewidth=0.8)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_volatility(returns):
    vol = returns.std() * (252 ** 0.5)
    vol.plot(kind="bar", figsize=(8, 5))
    plt.title("Annual Volatility by Asset")
    plt.ylabel("Volatility")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_correlation(returns):
    corr = returns.corr()
    corr.index.name = None
    corr.columns.name = None
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,        # muestra el número dentro de cada celda
        fmt=".2f",         # 2 decimales
        cmap="RdYlGn",     # rojo = correlación baja, verde = alta
        vmin=-1, vmax=1,   # rango fijo entre -1 y 1
        linewidths=0.5     # líneas entre celdas
    )
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()