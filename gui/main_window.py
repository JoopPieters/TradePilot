
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QDialog,
    QLabel,
    QFormLayout,
    QPushButton,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt

from PySide6.QtCore import QThread

from PySide6.QtGui import QColor

from PySide6.QtWidgets import QFormLayout

from scanner.scanner import scan

from gui.detail_window import DetailWindow

from gui.scan_worker import ScanWorker

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("TradePilot Professional")
        self.resize(1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QFormLayout()
        central_widget.setLayout(layout)

        titel = QLabel("TradePilot Professional")
        titel.setAlignment(Qt.AlignCenter)
       
        layout.addRow(titel)

        self.scan_button = QPushButton("▶ Scan Markt")
        self.scan_button.clicked.connect(self.scan_market)
        layout.addRow(self.scan_button)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Ticker",
            "Prijs",
            "Day",
            "Swing",
            "Invest",
            "RSI",
            "Status"
        ])
              
        self.best_day = QLabel("🟢 Beste Daytrade: -")
        self.best_swing = QLabel("🔵 Beste Swing: -")
        self.best_invest = QLabel("🟣 Beste Investering: -")

        layout.addRow(self.best_day)
        layout.addRow(self.best_swing)
        layout.addRow(self.best_invest)
        layout.addRow(self.table)
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
       
        self.scan_button.setEnabled(False)

        self.status.showMessage("Scannen...")

        self.table.setRowCount(0)

        self.thread = QThread()
        self.worker = ScanWorker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.scan_finished)
        self.worker.finished.connect(self.thread.quit)

        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()

    def scan_finished(self, resultaten):

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

            if aandeel["score_daytrade"] >= 80:
                status = "Bullish"

            elif aandeel["score_daytrade"] >= 60:
                status = "Neutraal"

            else:
                status = "Bearish"
           
            self.table.setItem(row, 6, self.status_item(status))

        self.scan_button.setEnabled(True)
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
 

    def __lt__(self, other):
        return self.volgorde[self.text()] < self.volgorde[other.text()]

    def status_item(self, status):
              
        item = QTableWidgetItem(status)

        item.setTextAlignment(Qt.AlignCenter)

        font = item.font()
        font.setBold(True)
        item.setFont(font)

        if status == "Bullish":
            item.setBackground(QColor("#006400"))
            item.setForeground(QColor("#FFFFFF"))

        elif status == "Neutraal":
            item.setBackground(QColor("#B8860B"))
            item.setForeground(QColor("#000000"))

        else:
            # item.setBackground(QColor("#8B0000"))
            # item.setForeground(QColor("#FFFFFF"))

            item.setBackground(QColor("#8B0000"))
            item.setForeground(QColor("#FFFFFF"))
        
        return item