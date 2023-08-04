import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 创建图表、显示文本设置为 "Exit"、快捷键为&后的第一个字母"E"（在windows有效,E会有下划线）
        exitAct = QAction(QIcon('java.png'), '&Exit', self)
        # setShortcut 方法用于独立设置菜单项的快捷键，和上面的E快捷键不一样，这个不需要打开菜单就能生效，上面的需要点开菜单
        exitAct.setShortcut('Ctrl+U')
        # 当用户将鼠标悬停在该动作上时，会在状态栏显示此提示信息
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        # menuBar()创建菜单栏。
        # 这里创建了一个菜单栏，并用addMenu()在上面添加了一个file菜单，用addAction()关联了点击退出应用的事件。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        # 在某些操作系统中，应用程序窗口默认具有一个原生的菜单栏，可以包含各种菜单项和操作。
        # 然而，有时候我们可能想要自定义应用程序的菜单栏，并使用自己创建的菜单项和操作。
        # 这时，就可以使用menubar.setNativeMenuBar(False)来禁用原生菜单栏，以便自定义菜单栏能够显示出来。
        # macos需要加这一句
        menubar.setNativeMenuBar(False)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())