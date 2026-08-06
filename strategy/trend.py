def bepaal_trend(ema, macd, signaal, rsi):

    score = 0

    if ema["EMA20"] > ema["EMA50"]:
        score += 1

    if macd > signaal:
        score += 1

    if 50 <= rsi <= 70:
        score += 1

    if score == 3:
        tekst = "🟢 Sterk stijgend"
    elif score == 2:
        tekst = "🟢 Stijgend"
    elif score == 1:
        tekst = "🟡 Neutraal"
    else:
        tekst = "🔴 Dalend"

    return {
        "tekst": tekst,
        "score": score
    }