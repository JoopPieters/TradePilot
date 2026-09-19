import yfinance as yf
import pandas as pd

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
        openingskoers = float(historie["Open"].iloc[-1])

        return {
            "ticker": ticker,
            "prijs": slotkoers,
            "open": openingskoers,
            "historie": historie
        }

    except Exception as fout:
        print(f"Fout bij {ticker}: {fout}")
        return None


def haal_invest_data_op(ticker):
    """Haal ongeveer 5 jaar historische weekdata op voor de investstrategie."""
    try:
        aandeel = yf.Ticker(ticker)
        historie = aandeel.history(period="5y", interval="1wk")

        if historie.empty:
            return None

        return historie

    except Exception as fout:
        print(f"Fout bij investdata {ticker}: {fout}")
        return None

def haal_laatste_afgesloten_week(ticker):
    """Haal weekdata op en gebruik alleen de laatst volledig afgesloten week."""
    try:
        aandeel = yf.Ticker(ticker)
        historie = aandeel.history(period="5y", interval="1wk")

        if historie.empty:
            return None

        vandaag = pd.Timestamp.now(tz=historie.index.tz)

        # Yahoo labelt de week met de maandag.
        # Een week is volledig afgesloten na vrijdag.
        afgesloten = historie[
            (historie.index + pd.Timedelta(days=4)) < vandaag
        ]

        if afgesloten.empty:
            return None

        return afgesloten

    except Exception as fout:
        print(f"Fout bij afgesloten week {ticker}: {fout}")
        return None
    
def haal_marktdata_op():
    """Haal belangrijke algemene marktgegevens op."""

    tickers = {
        "nasdaq": "^IXIC",
        "sp500": "^GSPC",
        "semiconductor": "^SOX",
        "nasdaq_futures": "NQ=F",
        "sp500_futures": "ES=F",
        "eur_usd": "EURUSD=X",
        "us10y": "^TNX",
    }

    resultaten = {}

    for naam, ticker in tickers.items():
        try:
            aandeel = yf.Ticker(ticker)
            historie = aandeel.history(period="5d")

            if historie.empty or len(historie) < 2:
                resultaten[naam] = None
                continue

            laatste = float(historie["Close"].iloc[-1])
            vorige = float(historie["Close"].iloc[-2])

            verandering = ((laatste - vorige) / vorige) * 100

            resultaten[naam] = {
                "ticker": ticker,
                "waarde": laatste,
                "verandering_pct": verandering,
            }

        except Exception as fout:
            print(f"Fout bij marktdata {ticker}: {fout}")
            resultaten[naam] = None

    return resultaten