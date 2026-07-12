from datetime import datetime

from scanner.scanner import scan
from strategy.advisor import geef_advies

from database.database import maak_database, sla_scan_op
from reports.terminal_report import toon_dashboard
from reports.csv_export import exporteer_csv

from logger import log


def main():

    maak_database()

    resultaten = scan()

    for aandeel in resultaten:

        score_day = aandeel["score_daytrade"]
        score_swing = aandeel["score_swing"]
        score_invest = aandeel["score_invest"]

        advies = geef_advies(
            score_day,
            score_swing,
            score_invest,
        )

        aandeel["advies"] = advies

        sla_scan_op(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            aandeel["ticker"],
            aandeel["prijs"],

            score_day,
            score_swing,
            score_invest,

            advies["beste_strategie"],
            advies["oordeel"],

            aandeel["rsi"],
            aandeel["ema20"],
            aandeel["ema50"],
            aandeel["macd"],
            aandeel["signaal"],
        )

        log(
            f"{aandeel['ticker']} "
            f"Day={score_day} "
            f"Swing={score_swing} "
            f"Invest={score_invest}"
        )

    toon_dashboard(resultaten)

    exporteer_csv(resultaten)


if __name__ == "__main__":
    main()