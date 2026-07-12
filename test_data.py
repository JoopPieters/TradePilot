import yfinance as yf

ticker = yf.Ticker("ASML.AS")

historie = ticker.history(period="10d")

print(historie[["Open", "High", "Low", "Close", "Volume"]])
