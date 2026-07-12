import yfinance as yf


def lees_watchlist(bestand="watchlist.txt"):
    """Lees alle tickers uit het watchlist-bestand."""
    with open(bestand, "r") as f:
        return [regel.strip() for regel in f if regel.strip()]


def haal_koers_op(ticker):
    """Haal de laatste slotkoers op via historische data."""
    try:
        aandeel = yf.Ticker(ticker)
        historie = aandeel.history(period="6mo")

        if historie.empty:
            return None

        slotkoers = float(historie["Close"].iloc[-1])

        return {
            "ticker": ticker,
            "prijs": slotkoers,
            "historie": historie
        }

    except Exception as fout:
        print(f"Fout bij {ticker}: {fout}")
        return None
