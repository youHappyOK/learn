# from ..view.ControllerView import *
#
# 一个模块必须有包结构且只能导入它的顶层模块内部的模块。
# 所以，如果一个模块被直接运行，则它自己为顶层模块，不存在层次结构，所以找不到其他的相对路径，
# 所以如果直接运行python xx.py ，而xx.py有相对导入就会报错
from practice.view.ControllerView import *
from practice.service.SettingService import *
from practice.service.AccountService import *
from practice.thead.ThreadProcess import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox



class ControllerViewSlot(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.iniRepo = IniFileRepository()
        self.settingService = SettingService(self.iniRepo)
        self.accountService = AccountService(self.iniRepo)
        self.threadProcess = ThreadProcess()

    def getMainTask(self):
        self.settingService.mainTask = ''
        if self.checkBox.checkState() == Qt.Checked:
            self.settingService.mainTask += self.checkBox.text() + ','
        if self.checkBox_2.checkState() == Qt.Checked:
            self.settingService.mainTask += self.checkBox_2.text() + ','
        if self.checkBox_3.checkState() == Qt.Checked:
            self.settingService.mainTask += self.checkBox_3.text() + ','
        # 截取','
        if self.settingService.mainTask.endswith(','):
            self.settingService.mainTask = self.settingService.mainTask[:-1]
        print('主线任务复选框变动', self.settingService.mainTask)

    def showAccount(self):
        print('加载账号信息...')
        # 先清空，再加载
        self.tableWidget.setRowCount(0)
        accountInfo = self.accountService.readAccount()
        if accountInfo:
            for row, rowList in enumerate(accountInfo):
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for col, item in enumerate(rowList):
                    tableWidgetItem = QtWidgets.QTableWidgetItem(str(item))
                    tableWidgetItem.setTextAlignment(Qt.AlignCenter)
                    if col == 0:
                        self.tableWidget.setItem(row, 3, tableWidgetItem)
                    if col == 1:
                        self.tableWidget.setItem(row, 4, tableWidgetItem)
                    if col == 2:
                        self.tableWidget.setItem(row, 5, tableWidgetItem)

    def getSideTask(self):
        self.settingService.sideTask = ''
        if self.checkBox_4.checkState() == Qt.Checked:
            self.settingService.sideTask += self.checkBox_4.text() + ','
        if self.checkBox_5.checkState() == Qt.Checked:
            self.settingService.sideTask += self.checkBox_5.text() + ','
        if self.checkBox_6.checkState() == Qt.Checked:
            self.settingService.sideTask += self.checkBox_6.text() + ','
        # 截取','
        if self.settingService.sideTask.endswith(','):
            self.settingService.sideTask = self.settingService.sideTask[:-1]
        print('支线任务复选框变动', self.settingService.sideTask)

    def getDailyTask(self):
        if self.radioButton.isChecked():
            self.settingService.dailyTask = self.radioButton.text()
        if self.radioButton_2.isChecked():
            self.settingService.dailyTask = self.radioButton_2.text()
        if self.radioButton_3.isChecked():
            self.settingService.dailyTask = self.radioButton_3.text()
        print('日常任务单选框变动', self.settingService.dailyTask)

    # 点击保存按钮槽函数
    # my_slot 方法被使用 @pyqtSlot(int) 装饰器声明为一个槽，它只接受一个整数类型的参数。这样做可以确保连接信号和槽时，参数类型匹配，从而避免可能的问题
    # @pyqtSlot中的参数填错，可能导致不执行
    # 加@pyqtSlot()保证只执行一次，有些QWidget有两个信号，信号：clicked()、clicked(bool)有两个，所以执行了两遍。
    @pyqtSlot(bool)
    def on_pushButton_5_clicked(self):
        self.settingService.saveSettingToFile()

    # 编辑程序位置文本框槽函数
    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        print('程序位置', text)
        self.settingService.progressPath = text.strip()

    # 编辑账号位置文本框槽函数
    @pyqtSlot(str)
    def on_lineEdit_2_textChanged(self, text):
        print('账号位置', text)
        self.settingService.accountPath = text.strip()

    # 多开数量
    @pyqtSlot(str)
    def on_lineEdit_3_textChanged(self, text):
        print('多开数量', text)
        self.settingService.runNum = text.strip()

    # 启动延迟
    @pyqtSlot(str)
    def on_lineEdit_4_textChanged(self, text):
        print('启动延迟数量', text)
        self.settingService.delayNum = text.strip()

    # 主线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_stateChanged(self):
        self.getMainTask()

    # 主线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_2_stateChanged(self):
        self.getMainTask()

    # 主线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_3_stateChanged(self):
        self.getMainTask()

    # 支线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_4_stateChanged(self):
        self.getSideTask()

    # 支线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_5_stateChanged(self):
        self.getSideTask()

    # 支线checkbox选择状态改变
    @pyqtSlot(int)
    def on_checkBox_6_stateChanged(self):
        self.getSideTask()

    # 日常任务选择状态改变
    # radio_button_clicked函数被@pyqtSlot()装饰器标记，而不需要指定任何参数类型，因为clicked事件不传递参数。当单选按钮被点击时，该函数会被调用，并输出一条消息
    @pyqtSlot()
    def on_radioButton_clicked(self):
        self.getDailyTask()

    # 日常任务选择状态改变
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.getDailyTask()

    # 日常任务选择状态改变
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        self.getDailyTask()

    @pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self):
        print('循环任务下拉变动' + self.settingService.weeklyTask)
        self.settingService.weeklyTask = self.comboBox.currentText()

    @pyqtSlot(bool)
    def on_pushButton_6_clicked(self):
        print('加载按钮触发')
        self.settingService.readSetting()
        self.lineEdit.setText(self.settingService.progressPath)
        self.lineEdit_2.setText(self.settingService.accountPath)
        self.lineEdit_3.setText(self.settingService.runNum)
        self.lineEdit_4.setText(self.settingService.delayNum)
        # 设置主线任务复选框
        for mainTaskItem in self.settingService.mainTask.strip().split(','):
            if self.checkBox.text() == mainTaskItem:
                self.checkBox.setChecked(True)
            if self.checkBox_2.text() == mainTaskItem:
                self.checkBox_2.setChecked(True)
            if self.checkBox_3.text() == mainTaskItem:
                self.checkBox_3.setChecked(True)
        # 设置支线任务复选框
        for sideTaskItem in self.settingService.sideTask.strip().split(','):
            if self.checkBox_4.text() == sideTaskItem:
                self.checkBox_4.setChecked(True)
            if self.checkBox_5.text() == sideTaskItem:
                self.checkBox_5.setChecked(True)
            if self.checkBox_6.text() == sideTaskItem:
                self.checkBox_6.setChecked(True)
        # 设置日常任务单选框
        if self.radioButton.text() == self.settingService.dailyTask.strip():
            self.radioButton.setChecked(True)
        if self.radioButton_2.text() == self.settingService.dailyTask.strip():
            self.radioButton_2.setChecked(True)
        if self.radioButton_3.text() == self.settingService.dailyTask.strip():
            self.radioButton_3.setChecked(True)
        # 设置循环任务下拉框
        for index in range(self.comboBox.count()):
            item_text = self.comboBox.itemText(index)
            if item_text == self.settingService.weeklyTask:
                self.comboBox.setCurrentIndex(index)
                # 找到匹配项后可以直接跳出循环，如果需要设置多个选中项可以去掉此行
                break
        # 加载账号
        self.showAccount()

    # 启动线程
    @pyqtSlot(bool)
    def on_pushButton_clicked(self):
        print('启动线程')
        self.threadProcess.runProcessThread(1)

    @pyqtSlot(bool)
    def on_pushButton_2_clicked(self):
        print('暂停某个线程')
        self.threadProcess.pauseProcessThread(0)

    @pyqtSlot(bool)
    def on_pushButton_3_clicked(self):
        print('恢复某个线程')
        self.threadProcess.resumeProcessThread(0)

    @pyqtSlot(bool)
    def on_pushButton_4_clicked(self):
        print('停止某个线程')
        self.threadProcess.stopProcessThread(0)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


















