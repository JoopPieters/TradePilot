from strategy.advisor import geef_advies

advies = geef_advies(
    score_daytrade=45,
    score_swing=85,
    score_invest=95,
)

print("Day Trading :", advies["daytrade"])
print("Swing       :", advies["swing"])
print("Invest      :", advies["invest"])