from strategy.score_daytrade import bereken_score_daytrade
from strategy.score_swing import bereken_score_swing
from strategy.score_invest import bereken_score_invest


def analyseer_aandeel(prijs, ema, rsi, macd, signaal):

    score_daytrade, redenen_daytrade = bereken_score_daytrade(
        prijs,
        ema["EMA20"],      # Later vervangen door EMA9
        ema["EMA20"],
        rsi,
        macd,
        signaal,
    )

    score_swing, redenen_swing = bereken_score_swing(
        prijs,
        ema["EMA20"],
        ema["EMA50"],
        ema["EMA200"],
        rsi,
        macd,
        signaal,
    )

    score_invest, redenen_invest = bereken_score_invest(
        prijs,
        ema["EMA50"],
        ema["EMA200"],
        rsi,
        macd,
        signaal,
    )

    return {
        "daytrade": {
            "score": score_daytrade,
            "redenen": redenen_daytrade,
        },
        "swing": {
            "score": score_swing,
            "redenen": redenen_swing,
        },
        "invest": {
            "score": score_invest,
            "redenen": redenen_invest,
        },
    }