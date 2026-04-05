import matplotlib.pyplot as plt

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