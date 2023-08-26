#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: View.py
Author: luoji
Date: 2023/8/26
Description: 视图层
"""
from PyQt5.QtWidgets import QMainWindow

from practice_part2.common.Container import Container
from practice_part2.ui.Ui_MainWindow import Ui_MainWindow


class View(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 把 view 放到 ioc 容器中
        Container.set('View', self)
