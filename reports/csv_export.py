import csv
import os
from datetime import datetime


def exporteer_csv(resultaten):

    os.makedirs("reports", exist_ok=True)

    bestandsnaam = (
        f"reports/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_TradePilot.csv"
    )

    with open(bestandsnaam, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile, delimiter=";")

        writer.writerow([
            "Ticker",
            "Day",
            "Swing",
            "Invest",
            "Beste strategie",
            "Oordeel",
            "Prijs",
            "RSI",
            "EMA20",
            "EMA50",
            "MACD",
            "Signaal",
        ])

        for aandeel in resultaten:

            advies = aandeel["advies"]

            writer.writerow([
                aandeel["ticker"],
                aandeel["score_daytrade"],
                aandeel["score_swing"],
                aandeel["score_invest"],
                advies["beste_strategie"],
                advies["oordeel"],
                f"{aandeel['prijs']:.2f}",
                f"{aandeel['rsi']:.2f}",
                f"{aandeel['ema20']:.2f}",
                f"{aandeel['ema50']:.2f}",
                f"{aandeel['macd']:.4f}",
                f"{aandeel['signaal']:.4f}",
            ])

    print(f"\n📄 CSV opgeslagen: {bestandsnaam}")