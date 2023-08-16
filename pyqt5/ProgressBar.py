#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QProgressBar widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

'''
在 PyQt 中，QWidget 和 QMainWindow 是两个常用的窗口基类，它们之间存在一些区别。

功能差异：

QWidget 是一个普通的窗口部件（widget）基类，提供了基本的窗口功能。它通常用于创建简单的用户界面元素，如按钮、标签等。QWidget 本身并不包含菜单栏、工具栏和状态栏等高级功能。
QMainWindow 是一个主窗口基类，是继承自 QWidget 的子类。它提供了更强大的窗口功能，并适合用于创建复杂的应用程序界面。QMainWindow 包含一个菜单栏、工具栏、状态栏等组件，还可以将其他部件（widget）添加到主窗口的中心区域。
布局管理器的默认设置：

对于 QWidget，默认的布局管理器是 QVBoxLayout，即垂直布局管理器。
对于 QMainWindow，默认的布局管理器是 QMainWindow 的内置布局管理器，称为中央部件（central widget）。这意味着可以将其他部件添加到 QMainWindow 的中心区域，并使用内置的布局管理器进行自动调整和排列，方便构建复杂的界面。
使用场景：

当你只需要创建简单的窗口部件时，例如自定义的对话框或单个页面应用，可以使用 QWidget。
当你要创建一个复杂的应用程序界面，带有主菜单、工具栏和状态栏，并需要将其他部件嵌入到主窗口的中心区域时，可以使用 QMainWindow。
需要注意的是，QWidget 和 QMainWindow 都提供了许多类似的方法和属性，继承自相同的基类 QObject 和 QPaintDevice。它们都可以通过重写特定的方法来实现自定义的行为，并且可以与其他部件和布局一起使用来构建丰富的用户界面。选择使用哪个基类取决于你的需求和设计目标。
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


    # timerEvent重载方法
    # 一旦 QBasicTimer 启动并开始计时，当时间间隔到达时，就会触发定时器事件，从而调用 timerEvent() 方法。
    # 在 timerEvent() 方法中，我们检查当前的进度条值，增加进度条的步进，并更新进度条的显示。
    # 如果达到设定的最大值（100），我们停止定时器并修改按钮的文本为 "Finished"。
    # 也就是说100毫秒被调用一次
    def timerEvent(self, e):
        # print('i am called')
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 其中 100 是定时器的时间间隔（以毫秒为单位），self 是接收定时器事件的对象
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())