from PySide6.QtWidgets import QDialog, QFormLayout, QLabel


class DetailWindow(QDialog):

    def __init__(self, aandeel):
        super().__init__()

        self.setWindowTitle(aandeel["ticker"])
        self.resize(450, 350)

        layout = QFormLayout()

        layout.addRow(QLabel(f"Ticker: {aandeel['ticker']}"))
        layout.addRow(QLabel(f"Prijs: {aandeel['prijs']:.2f}"))
        layout.addRow(QLabel(f"Openingskoers: {aandeel['open']:.2f}"))
        if aandeel["boven_open"]:
            layout.addRow(QLabel("📈 Boven openingskoers"))
        else:
            layout.addRow(QLabel("📉 Onder openingskoers"))
        layout.addRow(QLabel(f"Daytrade: {aandeel['score_daytrade']}"))
        layout.addRow(QLabel(f"Swing: {aandeel['score_swing']}"))
        layout.addRow(QLabel(f"Invest: {aandeel['score_invest']}"))
        layout.addRow(QLabel(f"RSI: {aandeel['rsi']:.2f}"))
        layout.addRow(QLabel(f"EMA9: {aandeel['ema20']:.2f}"))
        layout.addRow(QLabel(f"EMA20: {aandeel['ema20']:.2f}"))
        layout.addRow(QLabel(f"EMA50: {aandeel['ema50']:.2f}"))
        layout.addRow(QLabel(f"MACD: {aandeel['macd']:.2f}"))
        layout.addRow(QLabel(f"Signaallijn: {aandeel['signaal']:.2f}"))
        layout.addRow("Trend:", QLabel(aandeel["trend"]))
        layout.addRow("Trendscore:", QLabel(f'{aandeel["trendscore"]}/3'))


        self.setLayout(layout)