# 先导入生成的Ui界面模块
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui2 import Ui_MainWindow2

import sys


# 继承
class ChildUiClass(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 这样继承之后 你就可以在本文件中书写自己的程序而不会被影响
# 这样继承还有个好处就是后面你需要本界面调用其他界面的时候也很好操作

# 在main函数中调用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    child_dlg = ChildUiClass()
    # 例如下面这一行信号与槽的调用其他界面显示
    # About_dlg = ABout()
    # child_dlg .softversion.triggered.connect(About_dlg.show)
    child_dlg.show()
    sys.exit(app.exec_())
