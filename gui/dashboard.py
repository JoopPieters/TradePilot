from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
    QVBoxLayout,
)
import sys


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TradePilot")
        self.resize(1000, 600)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Ticker",
            "Koers",
            "EMA20",
            "RSI",
            "Score",
            "Advies"
        ])

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def voeg_rij_toe(self, ticker, koers, ema20, rsi, score):
        advies = "KOPEN" if score >= 80 else "VOLGEN"

        rij = self.table.rowCount()
        self.table.insertRow(rij)

        self.table.setItem(rij, 0, QTableWidgetItem(ticker))
        self.table.setItem(rij, 1, QTableWidgetItem(f"{koers:.2f}"))
        self.table.setItem(rij, 2, QTableWidgetItem(f"{ema20:.2f}"))
        self.table.setItem(rij, 3, QTableWidgetItem(f"{rsi:.2f}"))
        self.table.setItem(rij, 4, QTableWidgetItem(str(score)))
        self.table.setItem(rij, 5, QTableWidgetItem(advies))


def start_dashboard(data):
    app = QApplication(sys.argv)

    venster = Dashboard()

    for item in data:
        venster.voeg_rij_toe(
            item["ticker"],
            item["prijs"],
            item["ema20"],
            item["rsi"],
            item["score"],
        )

    venster.show()
    app.exec()
