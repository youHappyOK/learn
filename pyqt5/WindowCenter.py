import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        # 计算桌面的中心位置
        cp = QDesktopWidget().availableGeometry().center()
        # 通过 qr.moveCenter(cp) 将小部件的几何形状的中心移动到桌面的中心
        qr.moveCenter(cp)
        # self.move(qr.topLeft()) 是用于实际移动小部件到指定位置的代码。它将小部件的左上角移动到 qr（几何形状）的左上角位置。
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())