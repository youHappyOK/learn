import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # setFont()这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 鼠标悬停时展示在QWidget现实
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        # 鼠标悬停在button时展示
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())