import pandas as pd


def bereken_ema(data, periode):
    """
    Bereken de laatste EMA-waarde.
    """
    return float(data.ewm(span=periode, adjust=False).mean().iloc[-1])


def alle_ema(data):
    """
    Bereken EMA20, EMA50 en EMA200.
    """
    return {
        "EMA20": bereken_ema(data, 20),
        "EMA50": bereken_ema(data, 50),
        "EMA200": bereken_ema(data, 200)
    }
