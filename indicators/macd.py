import pandas as pd


def bereken_macd(data):
    """
    Bereken de laatste MACD-waarde en de signaallijn.
    Geeft (macd, signaal) terug.
    """
    ema12 = data.ewm(span=12, adjust=False).mean()
    ema26 = data.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26
    signaal = macd.ewm(span=9, adjust=False).mean()

    return float(macd.iloc[-1]), float(signaal.iloc[-1])
