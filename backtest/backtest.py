from data.yahoo import haal_koers_op


def eenvoudige_backtest(ticker):
    gegevens = haal_koers_op(ticker)

    if gegevens is None:
        return None

    historie = gegevens["historie"]["Close"]

    if len(historie) < 30:
        return None

    aankoop = historie.iloc[-11]
    verkoop = historie.iloc[-1]

    rendement = ((verkoop - aankoop) / aankoop) * 100

    return {
        "ticker": ticker,
        "aankoop": float(aankoop),
        "verkoop": float(verkoop),
        "rendement": float(rendement),
    }
