import pandas as pd


def bereken_rsi(data, periode=14):
    delta = data.diff()

    winst = delta.clip(lower=0)
    verlies = -delta.clip(upper=0)

    gemiddelde_winst = winst.rolling(window=periode).mean()
    gemiddelde_verlies = verlies.rolling(window=periode).mean()

    rs = gemiddelde_winst / gemiddelde_verlies

    rsi = 100 - (100 / (1 + rs))

    return float(rsi.iloc[-1])
