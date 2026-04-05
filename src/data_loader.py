import yfinance as yf

def get_data(tickers,start="2020-01-01",end="2026-04-05"):
    data=yf.download(tickers,start=start,end=end)["Close"]
    return data