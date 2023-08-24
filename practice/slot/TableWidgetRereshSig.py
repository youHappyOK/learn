from PyQt5.QtCore import pyqtSignal, QObject


class TableWidgetRereshSig(QObject):
        tableWidgetRereshSig = pyqtSignal(str)