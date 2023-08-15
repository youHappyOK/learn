import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        # 使用 setCentralWidget 方法，你可以将一个小部件设置为主窗口的中心部件，从而铺满主窗口的中心区域
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('java.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+U')
        # 当用户将鼠标悬停在该动作上时，会在状态栏显示此提示信息
        exitAct.setStatusTip('Exit application')

        # self.close() 只关闭当前窗口，而 QApplication.quit() 则退出整个应用程序
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        # macos需要加这一句
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())