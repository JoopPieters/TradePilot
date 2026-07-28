from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)
from PySide6.QtCore import Qt

from scanner.scanner import scan

from gui.detail_window import DetailWindow

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
              
        self.best_day = QLabel("🟢 Beste Daytrade: -")
        self.best_swing = QLabel("🔵 Beste Swing: -")
        self.best_invest = QLabel("🟣 Beste Investering: -")

        layout.addWidget(self.best_day)
        layout.addWidget(self.best_swing)
        layout.addWidget(self.best_invest)
        layout.addWidget(self.table)
        self.resultaten = []
        self.table.cellDoubleClicked.connect(self.open_detail)

        self.status = QStatusBar()
        self.status.showMessage("Gereed")
        self.setStatusBar(self.status)
        self.table.setSortingEnabled(True)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def open_detail(self, row, column):
        if not self.resultaten:
            return

        venster = DetailWindow(self.resultaten[row])
        venster.exec()

    def scan_market(self):

        self.status.showMessage("Scannen...")

        resultaten = scan()
        self.resultaten = resultaten
        
        self.table.setRowCount(len(resultaten))
        self.table.resizeRowsToContents()

        for row, aandeel in enumerate(resultaten):
            self.table.setItem(row, 0, QTableWidgetItem(aandeel["ticker"]))
            self.table.setItem(row, 1, QTableWidgetItem(f'{aandeel["prijs"]:.2f}'))
            self.table.setItem(row, 2, QTableWidgetItem(str(aandeel["score_daytrade"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(aandeel["score_swing"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(aandeel["score_invest"])))
            self.table.setItem(row, 5, QTableWidgetItem(f'{aandeel["rsi"]:.2f}'))

        if resultaten:

            beste_day = max(resultaten, key=lambda x: x["score_daytrade"])
            beste_swing = max(resultaten, key=lambda x: x["score_swing"])
            beste_invest = max(resultaten, key=lambda x: x["score_invest"])

            self.best_day.setText(
                f"🟢 Beste Daytrade: {beste_day['ticker']} ({beste_day['score_daytrade']})"
            )

            self.best_swing.setText(
                f"🔵 Beste Swing: {beste_swing['ticker']} ({beste_swing['score_swing']})"
            )

            self.best_invest.setText(
                f"🟣 Beste Investering: {beste_invest['ticker']} ({beste_invest['score_invest']})"
            )
        
        
        self.status.showMessage(f"{len(resultaten)} aandelen gescand.")

    def open_detail(self, row, column):
        if not self.resultaten:
            print("Geen resultaten")
            return

        print("Stap 2")

        venster = DetailWindow(self.resultaten[row])

        print("Stap 3")

        venster.exec()

        print("Stap 4")