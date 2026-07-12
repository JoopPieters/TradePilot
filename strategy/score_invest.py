def bereken_score_invest(
    prijs,
    ema50,
    ema200,
    rsi,
    macd,
    signaal,
):

    score = 0
    redenen = []

    if prijs > ema200:
        score += 30
        redenen.append("Boven EMA200")

    if ema50 > ema200:
        score += 25
        redenen.append("EMA50 boven EMA200")

    if 45 <= rsi <= 65:
        score += 15
        redenen.append("RSI stabiel")

    if macd > signaal:
        score += 10
        redenen.append("MACD positief")

    if prijs > ema50:
        score += 20
        redenen.append("Boven EMA50")

    return score, redenen