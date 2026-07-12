def bereken_score_swing(prijs, ema20, ema50, ema200, rsi, macd, signaal):

    score = 0
    redenen = []

    if prijs > ema20:
        score += 10
        redenen.append("Boven EMA20")

    if prijs > ema50:
        score += 15
        redenen.append("Boven EMA50")

    if prijs > ema200:
        score += 20
        redenen.append("Boven EMA200")

    if ema20 > ema50:
        score += 15
        redenen.append("EMA20 boven EMA50")

    if 50 <= rsi <= 65:
        score += 20
        redenen.append("RSI gezond")

    if macd > signaal:
        score += 20
        redenen.append("MACD bullish")

    return score, redenen
