# TradePilot Architectuur

## Hoofdmodules

main.py
Start het programma.

scanner/
Leest de watchlist en haalt marktgegevens op.

data/
Verzorgt alle gegevensbronnen (Yahoo, later ook andere bronnen).

indicators/
Berekent EMA, RSI, MACD, ATR, Volume enzovoort.

strategy/
Bevat alle strategieën.

engine.py
Combineert indicatoren en strategieën tot één analyse.

advisor.py
Zet analyses om in begrijpelijke adviezen.

database/
Slaat scans, snapshots en historische resultaten op.

backtest/
Test strategieën op historische data.

reports/
Maakt rapporten.

tests/
Test iedere module afzonderlijk.

docs/
Documentatie en ontwerp.