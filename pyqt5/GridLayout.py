#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a skeleton
of a calculator using a QGridLayout.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            # addWidget的第二个参数是可变参数，所以要加*
            # 如果只有一个参数，例如 grid.addWidget(widget, 0)，则小部件将被放置在第 0 行。
            # 如果有两个参数，例如 grid.addWidget(widget, 1, 2)，则小部件将被放置在第 1 行、第 2 列的位置
            # 如果有更多的参数，例如 grid.addWidget(widget, 2, 1, 3)，则小部件将被放置在第 2 行、第 1 列，跨越 3 个行的位置(就是占三行)
            # 跨列就是4个数字参数
            grid.addWidget(button, *position)

        self.move(600, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())