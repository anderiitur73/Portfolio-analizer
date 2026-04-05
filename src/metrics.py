import pandas as pd
import numpy as np


def daily_returns(data):
    return data.pct_change().dropna()
    
def cumulative_returns(returns):
    return (1+returns).cumprod()

def volatility(returns):
    return returns.std()*np.sqrt(252)

def sharpe_ratio(returns,risk_free=0.04):
    excess_returns=returns-risk_free/252
    return (excess_returns.mean() / returns.std()) * np.sqrt(252)

def max_drawdown(cum_returns):
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()

def portfolio_returns(returns, weights):
    return returns.dot(weights)