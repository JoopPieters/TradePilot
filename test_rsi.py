import yfinance as yf
from indicators.rsi import bereken_rsi

ticker = yf.Ticker("ASML.AS")
historie = ticker.history(period="6mo")

rsi = bereken_rsi(historie["Close"])

print(f"RSI = {rsi:.2f}")
