from PyQt5.QtCore import pyqtSignal, QObject


class TextEditRereshSig(QObject):
        textEditRereshSig = pyqtSignal(str)