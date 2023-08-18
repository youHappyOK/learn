# from ..view.ControllerView import *
#
# 一个模块必须有包结构且只能导入它的顶层模块内部的模块。
# 所以，如果一个模块被直接运行，则它自己为顶层模块，不存在层次结构，所以找不到其他的相对路径，
# 所以如果直接运行python xx.py ，而xx.py有相对导入就会报错
from practice.view.ControllerView import *
from practice.repository.SettingRepository import *
from PyQt5.QtCore import Qt


class ControllerViewSlot(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.settingRepository = SettingRepository()

    def getMainTaskCheckBox(self):
        if self.checkBox.checkState() == Qt.Checked:
            self.settingRepository.mainTask += self.checkBox.text()
        if self.checkBox_2.checkState() == Qt.Checked:
            self.settingRepository.mainTask += self.checkBox.text()
        if self.checkBox_3.checkState() == Qt.Checked:
            self.settingRepository.mainTask += self.checkBox.text()

    # 点击保存按钮槽函数
    @QtCore.pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.settingRepository.saveSettingToFile()

    # 编辑程序位置文本框槽函数
    @QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        self.settingRepository.progressPath = text.strip()

    # 编辑账号位置文本框槽函数
    @QtCore.pyqtSlot(str)
    def on_lineEdit_2_textChanged(self, text):
        self.settingRepository.accountPath = text.strip()

    # 多开数量
    @QtCore.pyqtSlot(str)
    def on_lineEdit_3_textChanged(self, text):
        self.settingRepository.runNum = int(text.strip)

    # 启动延迟
    @QtCore.pyqtSlot(str)
    def on_lineEdit_3_textChanged(self, text):
        self.settingRepository.delayNum = int(text.strip)


    # 主线checkbox选择状态改变
    @QtCore.pyqtSlot()
    def on_checkBox_stateChanged(self):
        self.getMainTaskCheckBox()

    # 主线checkbox选择状态改变
    @QtCore.pyqtSlot()
    def on_checkBox_2_stateChanged(self):
        self.getMainTaskCheckBox()

    # 主线checkbox选择状态改变
    @QtCore.pyqtSlot()
    def on_checkBox_3_stateChanged(self):
        self.getMainTaskCheckBox()




