# 先导入生成的Ui界面模块
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ControllerUi import Ui_MainWindow


class ChildControllerUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ChildControllerUi()
    ui.show()
    sys.exit(app.exec_())
