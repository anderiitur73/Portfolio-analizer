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
    corr= returns.corr().round(4)
    corr.index.name = None
    corr.columns.name = None
    return corr

def interpret_portfolio(port_ret, market_ret, port_cum, market_cum):
    p_sharpe = sharpe_ratio(port_ret)
    m_sharpe = sharpe_ratio(market_ret)
    p_vol = volatility(port_ret)
    m_vol = volatility(market_ret)
    p_dd = max_drawdown(port_cum)
    m_dd = max_drawdown(market_cum)
    p_ret = port_cum.iloc[-1] - 1
    m_ret = market_cum.iloc[-1] - 1

    lines = []

    # Rentabilidad
    if p_ret > m_ret:
        lines.append(f"Your portfolio returned {p_ret:.1%} vs {m_ret:.1%} for SPY — you beat the market.")
    else:
        lines.append(f"Your portfolio returned {p_ret:.1%} vs {m_ret:.1%} for SPY — SPY outperformed you.")

    # Sharpe
    if p_sharpe > m_sharpe:
        lines.append(f"Better risk-adjusted return: Sharpe {p_sharpe:.2f} vs {m_sharpe:.2f} (SPY).")
    else:
        lines.append(f"Worse risk-adjusted return: Sharpe {p_sharpe:.2f} vs {m_sharpe:.2f} (SPY).")

    # Volatilidad
    if p_vol < m_vol:
        lines.append(f"Lower volatility: {p_vol:.1%} vs {m_vol:.1%} (SPY).")
    else:
        lines.append(f"Higher volatility: {p_vol:.1%} vs {m_vol:.1%} (SPY).")

    # Drawdown
    if p_dd > m_dd:
        lines.append(f"Better max drawdown: {p_dd:.1%} vs {m_dd:.1%} (SPY).")
    else:
        lines.append(f"Worse max drawdown: {p_dd:.1%} vs {m_dd:.1%} (SPY).")

    return "\n".join(lines)