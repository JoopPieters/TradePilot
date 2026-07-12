def bereken_score_daytrade(prijs, ema9, ema20, rsi, macd, signaal):

    score = 0
    redenen = []

    if prijs > ema9:
        score += 25
        redenen.append("Boven EMA9")

    if prijs > ema20:
        score += 20
        redenen.append("Boven EMA20")

    if 45 <= rsi <= 70:
        score += 20
        redenen.append("RSI actief")

    if macd > signaal:
        score += 20
        redenen.append("MACD bullish")

    if ema9 > ema20:
        score += 15
        redenen.append("EMA9 boven EMA20")

    return score, redenen