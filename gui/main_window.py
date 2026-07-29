
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

from PySide6.QtGui import QColor

from PySide6.QtGui import QFont

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
         # titel.setStyleSheet("""
         #   font-size:24px;
         #   font-weight:bold;
         #   padding:20px;
         #""")
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
        self.setStyleSheet("""
        QMainWindow {
            background-color: #2b2b2b;
        }

        QWidget {
            background-color: #2b2b2b;
            color: white;
            font-size: 11pt;
        }

        QLabel {
            color: white;
            font-size: 11pt;
            font-weight: bold;
        }

        QPushButton {
            background-color: #3c3f41;
            color: white;
            border: 1px solid #555;
            border-radius: 6px;
            padding: 8px;
            font-size: 11pt;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #4c5052;
        }

        QTableWidget {
            background-color: #1e1e1e;
            color: white;
            gridline-color: #444;
            font-size: 11pt;
            alternate-background-color: #252526;
            selection-background-color: #0078d7;
            selection-color: white;
        }

        QHeaderView::section {
            background-color: #3c3f41;
            color: white;
            font-weight: bold;
            border: 1px solid #555;
            padding: 6px;
        }

        QStatusBar {
            color: white;
            background-color: #3c3f41;
        }
        """)
        
        self.table.setSortingEnabled(True)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
    
    def scan_market(self):
       
        self.status.showMessage("Scannen...")

        resultaten = scan()
        self.resultaten = resultaten
        
        self.table.setRowCount(len(resultaten))
        self.table.resizeRowsToContents()

        for row, aandeel in enumerate(resultaten):
            self.table.setItem(row, 0, QTableWidgetItem(aandeel["ticker"]))

            prijs_item = QTableWidgetItem(f'{aandeel["prijs"]:.2f}')
            prijs_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 1, prijs_item)

            self.table.setItem(
                row,
                2,
                self.kleur_score(aandeel["score_daytrade"])
            )

            self.table.setItem(
                row,
                3,
                self.kleur_score(aandeel["score_swing"])
            )

            self.table.setItem(
                row,
                4,
                self.kleur_score(aandeel["score_invest"])
            )

            rsi_item = QTableWidgetItem(f'{aandeel["rsi"]:.2f}')
            rsi_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 5, rsi_item)

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
            return
        
        self.detail_window = DetailWindow(self.resultaten[row])
        self.detail_window.show()
        
    def kleur_score(self, score):

        item = QTableWidgetItem(str(score))

        if score >= 80:
            item.setBackground(QColor("#006400"))   # donkergroen
            item.setForeground(QColor("#FFFFFF"))   # wit

        elif score >= 60:
            item.setBackground(QColor("#B8860B"))   # donker goud
            item.setForeground(QColor("#000000"))   # zwart

        else:
            item.setBackground(QColor("#8B0000"))   # donkerrood
            item.setForeground(QColor("#FFFFFF"))   # wit

        font = item.font()
        font.setBold(True)
        item.setFont(font)

        item.setTextAlignment(Qt.AlignCenter)

        return item
       