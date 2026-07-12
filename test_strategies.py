from strategy.score_daytrade import bereken_score_daytrade
from strategy.score_swing import bereken_score_swing
from strategy.score_invest import bereken_score_invest

prijs = 100
ema9 = 99
ema20 = 98
ema50 = 95
ema200 = 90
rsi = 55
macd = 1.5
signaal = 1.0

score_dt, _ = bereken_score_daytrade(
    prijs,
    ema9,
    ema20,
    rsi,
    macd,
    signaal,
)

score_sw, _ = bereken_score_swing(
    prijs,
    ema20,
    ema50,
    ema200,
    rsi,
    macd,
    signaal,
)

score_inv, _ = bereken_score_invest(
    prijs,
    ema50,
    ema200,
    rsi,
    macd,
    signaal,
)

print(f"Day Trading : {score_dt}")
print(f"Swing       : {score_sw}")
print(f"Invest      : {score_inv}")