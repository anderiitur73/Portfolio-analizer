from data_loader import get_data

tickers = ["SPY", "AAPL", "MSFT"]
data = get_data(tickers)

print(data.head())      # primeras 5 filas
print(data.shape)       # cuántas filas × columnas tienes
print(data.dtypes)      # tipo de dato de cada columna