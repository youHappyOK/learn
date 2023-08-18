import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from slot.ControllerViewSlot import *


class ApplicationBootstrp(QMainWindow, ControllerViewSlot):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    boostrap = ApplicationBootstrp()
    boostrap.show()
    sys.exit(app.exec_())
