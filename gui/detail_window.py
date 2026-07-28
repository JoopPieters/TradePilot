from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel


class DetailWindow(QDialog):

    def __init__(self, aandeel):
        super().__init__()

        self.setWindowTitle(aandeel["ticker"])
        self.resize(450, 350)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Ticker: {aandeel['ticker']}"))
        layout.addWidget(QLabel(f"Prijs: {aandeel['prijs']:.2f}"))
        layout.addWidget(QLabel(f"Daytrade: {aandeel['score_daytrade']}"))
        layout.addWidget(QLabel(f"Swing: {aandeel['score_swing']}"))
        layout.addWidget(QLabel(f"Invest: {aandeel['score_invest']}"))
        layout.addWidget(QLabel(f"RSI: {aandeel['rsi']:.2f}"))

        self.setLayout(layout)