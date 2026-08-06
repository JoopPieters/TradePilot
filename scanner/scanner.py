from data.yahoo import lees_watchlist, haal_koers_op
from indicators.ema import alle_ema
from indicators.rsi import bereken_rsi
from indicators.macd import bereken_macd
from strategy.engine import analyseer_aandeel
from strategy.trend import bepaal_trend

def scan():

    resultaten = []

    for ticker in lees_watchlist():

        gegevens = haal_koers_op(ticker)

        if gegevens is None:
            continue

        close = gegevens["historie"]["Close"]
        prijs = gegevens["prijs"]
        openingskoers = gegevens["open"]
        boven_open = prijs >= openingskoers

        ema = alle_ema(close)
        rsi = bereken_rsi(close)
        macd, signaal = bereken_macd(close)

        analyse = analyseer_aandeel(
            prijs,
            ema,
            rsi,
            macd,
            signaal,
        )

        trend = bepaal_trend(
        ema,
        macd,
        signaal,
        rsi,
        )

        resultaten.append({
            "ticker": ticker,
            "prijs": prijs,
            "open": openingskoers,
            "boven_open": boven_open,

            "score_daytrade": analyse["daytrade"]["score"],
            "score_swing": analyse["swing"]["score"],
            "score_invest": analyse["invest"]["score"],

            "redenen_daytrade": analyse["daytrade"]["redenen"],
            "redenen_swing": analyse["swing"]["redenen"],
            "redenen_invest": analyse["invest"]["redenen"],

            "rsi": rsi,
            "ema20": ema["EMA20"],
            "ema50": ema["EMA50"],
            "macd": macd,
            "signaal": signaal,
            "trend": trend["tekst"],
            "trendscore": trend["score"],
        })

        resultaten.sort(
            key=lambda x: x["score_swing"],
            reverse=True
        )

    return resultaten