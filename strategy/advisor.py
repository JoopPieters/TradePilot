def geef_advies(score_daytrade, score_swing, score_invest):

    strategieen = {
        "⚡ Day Trading": score_daytrade,
        "📈 Swing Trading": score_swing,
        "💼 Lang Beleggen": score_invest,
    }

    beste_strategie = max(strategieen, key=strategieen.get)
    beste_score = strategieen[beste_strategie]

    if beste_score >= 90:
        oordeel = "⭐⭐⭐⭐⭐ Zeer sterk"

    elif beste_score >= 75:
        oordeel = "⭐⭐⭐⭐ Sterk"

    elif beste_score >= 60:
        oordeel = "⭐⭐⭐ Redelijk"

    elif beste_score >= 40:
        oordeel = "⭐⭐ Zwak"

    else:
        oordeel = "⭐ Zeer zwak"

    return {
        "beste_strategie": beste_strategie,
        "beste_score": beste_score,
        "oordeel": oordeel,
    }