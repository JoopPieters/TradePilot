from PySide6.QtCore import QObject, Signal

from scanner.scanner import scan


class ScanWorker(QObject):

    finished = Signal(list)

    def run(self):
        resultaten = scan()
        self.finished.emit(resultaten)