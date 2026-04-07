import pandas as pd
import numpy as np


def daily_returns(data):
    return data.pct_change().dropna()
    
def cumulative_returns(returns):
    return (1+returns).cumprod()

def volatility(returns):
    return returns.std()*np.sqrt(252)

def sharpe_ratio(returns,risk_free=0.03):
    excess_returns=returns-risk_free/252
    return (excess_returns.mean() / returns.std()) * np.sqrt(252)

def max_drawdown(cum_returns):
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()

def portfolio_returns(returns, weights):
    return returns.dot(weights)

def sortino_ratio(returns,risk_free=0.03):
    excess_returns=returns-risk_free/252
    downside=np.minimum(returns,0)
    downside_std = np.sqrt((downside ** 2).mean())
    return excess_returns.mean()/downside_std*np.sqrt(252)

def beta_ratio(returns,market="SPY"):
    cov_mat=returns.cov()
    market_var=cov_mat[market][market]
    betas=cov_mat[market]/market_var
    return betas.drop(market)

def correlation_matrix(returns):
    return returns.corr().round(4)
