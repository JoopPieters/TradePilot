from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem
)
from PySide6.QtCore import Qt

from scanner.scanner import scan


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TradePilot Professional")
        self.resize(1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        titel = QLabel("TradePilot Professional")
        titel.setAlignment(Qt.AlignCenter)
        titel.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:20px;
        """)
        layout.addWidget(titel)

        self.scan_button = QPushButton("▶ Scan Markt")
        self.scan_button.clicked.connect(self.scan_market)
        layout.addWidget(self.scan_button)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Ticker",
            "Prijs",
            "Day",
            "Swing",
            "Invest",
            "RSI"
        ])
        layout.addWidget(self.table)

        self.status = QStatusBar()
        self.status.showMessage("Gereed")
        self.setStatusBar(self.status)

    def scan_market(self):

        self.status.showMessage("Scannen...")

        resultaten = scan()
        print(f"Aantal resultaten: {len(resultaten)}")

        if resultaten:
            print(resultaten[0])

        self.table.setRowCount(len(resultaten))

        for row, aandeel in enumerate(resultaten):
            self.table.setItem(row, 0, QTableWidgetItem(aandeel["ticker"]))
            self.table.setItem(row, 1, QTableWidgetItem(f'{aandeel["prijs"]:.2f}'))
            self.table.setItem(row, 2, QTableWidgetItem(str(aandeel["score_daytrade"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(aandeel["score_swing"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(aandeel["score_invest"])))
            self.table.setItem(row, 5, QTableWidgetItem(f'{aandeel["rsi"]:.2f}'))

        self.status.showMessage(f"{len(resultaten)} aandelen gescand.")