from data.yahoo import (
    lees_watchlist,
    haal_koers_op,
    haal_laatste_afgesloten_week,
)
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
        invest_data = haal_laatste_afgesloten_week(ticker)

        if invest_data is None:
            continue

        close = gegevens["historie"]["Close"]
        prijs = gegevens["prijs"]
        openingskoers = gegevens["open"]
        boven_open = prijs >= openingskoers
        invest_close = invest_data["Close"]
        invest_ema = alle_ema(invest_close)
        invest_rsi = bereken_rsi(invest_close)
        invest_macd, invest_signaal = bereken_macd(invest_close)

        ema = alle_ema(close)
        rsi = bereken_rsi(close)
        macd, signaal = bereken_macd(close)

        analyse = analyseer_aandeel(
            prijs,
            ema,
            rsi,
            macd,
            signaal,
            invest_close.iloc[-1],
            invest_ema,
            invest_rsi,
            invest_macd,
            invest_signaal,
        )

        trend = bepaal_trend(
        ema,
        macd,
        signaal,
        rsi,
        )

        if rsi is None:
            print(f"WAARSCHUWING: {ticker} heeft geen RSI")

        if analyse["swing"]["score"] is None:
            print(f"WAARSCHUWING: {ticker} heeft geen swingscore")

        if analyse["invest"]["score"] is None:
            print(f"WAARSCHUWING: {ticker} heeft geen investscore")
            
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
            "ema9": ema["EMA9"],
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