from PySide6.QtWidgets import QDialog, QFormLayout, QLabel


class DetailWindow(QDialog):

    def __init__(self, aandeel):
        super().__init__()

        self.setWindowTitle(aandeel["ticker"])
        self.resize(500, 500)

        layout = QFormLayout()

        # ===== Algemene gegevens =====

        layout.addRow(QLabel(f"Ticker: {aandeel['ticker']}"))
        layout.addRow(QLabel(f"Prijs: {aandeel['prijs']:.2f}"))
        layout.addRow(QLabel(f"Openingskoers: {aandeel['open']:.2f}"))

        if aandeel["boven_open"]:
            layout.addRow(QLabel("📈 Boven openingskoers"))
        else:
            layout.addRow(QLabel("📉 Onder openingskoers"))

        # ===== Scores =====

        layout.addRow(QLabel(f"Daytrade: {aandeel['score_daytrade']}"))
        layout.addRow(QLabel(f"Swing: {aandeel['score_swing']}"))
        layout.addRow(QLabel(f"Invest: {aandeel['score_invest']}"))

        # ===== Daggegevens =====

        layout.addRow(QLabel("── Daggegevens ──"))

        layout.addRow(
            QLabel(f"RSI: {aandeel['rsi']:.2f}")
        )

        layout.addRow(
            QLabel(f"EMA9: {aandeel['ema9']:.2f}")
        )

        layout.addRow(
            QLabel(f"EMA20: {aandeel['ema20']:.2f}")
        )

        layout.addRow(
            QLabel(f"EMA50: {aandeel['ema50']:.2f}")
        )

        layout.addRow(
            QLabel(f"MACD: {aandeel['macd']:.2f}")
        )

        layout.addRow(
            QLabel(f"Signaallijn: {aandeel['signaal']:.2f}")
        )

        # ===== Invest weekgegevens =====

        layout.addRow(QLabel("── Invest — laatste afgesloten week ──"))

        if aandeel["invest_prijs"] is not None:

            layout.addRow(
                QLabel(
                    f"Weekprijs: {aandeel['invest_prijs']:.2f}"
                )
            )

            layout.addRow(
                QLabel(
                    f"Week RSI: {aandeel['invest_rsi']:.2f}"
                )
            )

            layout.addRow(
                QLabel(
                    f"Week EMA50: {aandeel['invest_ema50']:.2f}"
                )
            )

            layout.addRow(
                QLabel(
                    f"Week EMA200: {aandeel['invest_ema200']:.2f}"
                )
            )

            layout.addRow(
                QLabel(
                    f"Week MACD: {aandeel['invest_macd']:.2f}"
                )
            )

            layout.addRow(
                QLabel(
                    f"Week signaallijn: {aandeel['invest_signaal']:.2f}"
                )
            )

        else:

            layout.addRow(
                QLabel("Geen invest-weekdata beschikbaar")
            )

        # ===== Trend =====

        layout.addRow(QLabel("── Trend ──"))

        layout.addRow(
            "Trend:",
            QLabel(aandeel["trend"])
        )

        layout.addRow(
            "Trendscore:",
            QLabel(f'{aandeel["trendscore"]}/3')
        )

        self.setLayout(layout)