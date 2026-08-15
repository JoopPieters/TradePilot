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