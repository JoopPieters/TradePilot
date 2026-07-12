from strategy.score import bereken_score

score, redenen = bereken_score(
    prijs=100,
    ema20=95,
    ema50=92,
    ema200=88,
    rsi=56,
    macd=2.3,
    signaal=1.9,
)

print(f"Score : {score}")
print()

for reden in redenen:
    print("✓", reden)
