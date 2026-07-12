import yfinance as yf
from indicators.macd import bereken_macd

ticker = yf.Ticker("ASML.AS")
historie = ticker.history(period="6mo")

macd, signaal = bereken_macd(historie["Close"])

print(f"MACD    : {macd:.3f}")
print(f"Signaal : {signaal:.3f}")
