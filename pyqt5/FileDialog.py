#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # 如果用户选择了文件（通过检查 fname 列表中的第一个元素是否存在），则打开该文件并读取其中的内容
        if fname[0]:
            f = open(fname[0], 'r')
            # with f: 是一个上下文管理器（Context Manager）的用法。
            # 当文件对象（f）作为上下文管理器时，使用 with 语句可以确保在执行完毕后正确地关闭文件。这样可以避免手动调用 f.close() 来关闭文件
            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())