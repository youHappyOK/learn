# 先导入生成的Ui界面模块
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from testQD import Ui_MainWindow


# 注意，在tab页中拖拽layout，他会在layout外面隐式再嵌套一个widget，所以转换后的py文件还需要手动改下，
# 直接tab.setLayout，忽略中间的widget
# 同理，groupBox_3也是一样
class ChildControllerUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ChildControllerUi()
    ui.show()
    sys.exit(app.exec_())
