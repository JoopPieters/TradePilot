from datetime import datetime


def toon_dashboard(resultaten):

    print()
    print("=" * 120)
    print(f"TradePilot v1.0-beta        {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("=" * 120)
    print(f"Aantal gescande aandelen : {len(resultaten)}")
    print()

    # -------- TOP 5 DAY --------

    print("TOP 5 DAY TRADING")
    print("-" * 40)

    top_day = sorted(
        resultaten,
        key=lambda x: x["score_daytrade"],
        reverse=True
    )[:5]

    for i, aandeel in enumerate(top_day, start=1):
        print(f"{i}. {aandeel['ticker']:<10} {aandeel['score_daytrade']:>3}")

    print()

    # -------- TOP 5 SWING --------

    print("TOP 5 SWING TRADING")
    print("-" * 40)

    top_swing = sorted(
        resultaten,
        key=lambda x: x["score_swing"],
        reverse=True
    )[:5]

    for i, aandeel in enumerate(top_swing, start=1):
        print(f"{i}. {aandeel['ticker']:<10} {aandeel['score_swing']:>3}")

    print()

    # -------- TOP 5 INVEST --------

    print("TOP 5 LANG BELEGGEN")
    print("-" * 40)

    top_invest = sorted(
        resultaten,
        key=lambda x: x["score_invest"],
        reverse=True
    )[:5]

    for i, aandeel in enumerate(top_invest, start=1):
        print(f"{i}. {aandeel['ticker']:<10} {aandeel['score_invest']:>3}")

    print()
    print("=" * 120)

    print(
        f"{'Ticker':<10}"
        f"{'Day':>6}"
        f"{'Swing':>8}"
        f"{'Invest':>9}"
        f"{'Prijs':>12}"
        f"{'RSI':>8}  "
        f"{'Strategie':<22}"
        f"{'Sterkte'}"
    )

    print("-" * 120)

    for aandeel in resultaten:

        advies = aandeel["advies"]

        print(
            f"{aandeel['ticker']:<10}"
            f"{aandeel['score_daytrade']:>6}"
            f"{aandeel['score_swing']:>8}"
            f"{aandeel['score_invest']:>9}"
            f"{aandeel['prijs']:>12.2f}"
            f"{aandeel['rsi']:>8.2f}  "
            f"{advies['beste_strategie']:<22}"
            f"{advies['oordeel']}"
        )

    print("=" * 120)