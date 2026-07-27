def bereken_score_daytrade(prijs, ema9, ema20, rsi, macd, signaal):

    score = 0
    redenen = []

    # ===== Trend =====

    if prijs > ema9:
        score += 20
        redenen.append("Boven EMA9")

        verschil = (prijs - ema9) / ema9 * 100

        if verschil > 2:
            score += 5
            redenen.append("Sterk boven EMA9")

    # ===== Middellange trend =====

    if prijs > ema20:
        score += 15
        redenen.append("Boven EMA20")

        verschil = (prijs - ema20) / ema20 * 100

        if verschil > 3:
            score += 5
            redenen.append("Sterk boven EMA20")

    # ===== RSI =====

    if 50 <= rsi <= 60:
        score += 20
        redenen.append("RSI ideaal")

    elif 45 <= rsi < 50:
        score += 15
        redenen.append("RSI goed")

    elif 60 < rsi <= 65:
        score += 10
        redenen.append("RSI loopt op")

    elif 65 < rsi <= 70:
        score += 5
        redenen.append("RSI hoog")

    # ===== MACD =====

    verschil = macd - signaal

    if verschil > 0:

        score += 15
        redenen.append("MACD bullish")

        if verschil > 0.5:
            score += 5
            redenen.append("Sterke MACD")

    # ===== EMA-kruising =====

    if ema9 > ema20:
        score += 15
        redenen.append("EMA9 boven EMA20")

    return min(score, 100), redenen