import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Ready')
        # self.setGeometry(300, 300, 250, 150) 设置小部件的几何形状时，(300, 300) 表示小部件的左上角相对于父窗口的位置，如果没有父窗口，那么就是桌面
        # 小部件的宽度为 250 像素，高度为 150 像素。
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())