#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: SlotFunc.py
Author: 吉姆哥
Date: 2023/8/26
Description: 槽函数
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from practice_part2.common.Container import Container


class SlotFunc:

    # 保存配置
    @staticmethod
    def saveSetting():
        view = Container.get('View')
        taskList = ''
        if view.checkBox.checkState() == Qt.Checked:
            taskList += view.checkBox.text() + ','
        if view.checkBox_2.checkState() == Qt.Checked:
            taskList += view.checkBox_2.text() + ','
        if view.checkBox_3.checkState() == Qt.Checked:
            taskList += view.checkBox_3.text() + ','
        # 截取','
        if taskList.endswith(','):
            taskList = taskList[:-1]
        Container.get('IniFileRepo').saveSettingToFile(view.lineEdit.text(), view.lineEdit_2.text(),
                                                       view.lineEdit_3.text(), taskList)

    # 加载配置
    @staticmethod
    def loadSetting(self):
        iniFileRepo = Container.get('IniFileRepo')
        view = Container.get('View')
        settingDict = iniFileRepo.readSetting()
        if settingDict:
            view.lineEdit.setText(settingDict['ldPath'])
            view.lineEdit_2.setText(settingDict['ldConsolePath'])
            view.lineEdit_3.setText(settingDict['accountPath'])
            if settingDict['taskList']:
                # 设置主线任务复选框
                for taskItem in settingDict['taskList'].strip().split(','):
                    if view.checkBox.text() == taskItem:
                        view.checkBox.setChecked(True)
                    if view.checkBox_2.text() == taskItem:
                        view.checkBox_2.setChecked(True)
                    if view.checkBox_3.text() == taskItem:
                        view.checkBox_3.setChecked(True)

    # 加载用户信息
    @staticmethod
    def loadAccount(self):
        print('加载账号信息')
        view = Container.get('View')
        iniFileRepo = Container.get('IniFileRepo')
        # 先清空，再加载
        view.tableWidget.setRowCount(0)
        accountInfo = iniFileRepo.readAccount()
        if accountInfo:
            for row, rowList in enumerate(accountInfo):
                row_position = view.tableWidget.rowCount()
                view.tableWidget.insertRow(row_position)
                for col, item in enumerate(rowList):
                    tableWidgetItem = QtWidgets.QTableWidgetItem(str(item))
                    tableWidgetItem.setTextAlignment(Qt.AlignCenter)
                    if col == 0:
                        view.tableWidget.setItem(row, 1, tableWidgetItem)
                    if col == 1:
                        view.tableWidget.setItem(row, 2, tableWidgetItem)
                    if col == 2:
                        view.tableWidget.setItem(row, 3, tableWidgetItem)


