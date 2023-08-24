import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from practice.slot.ControllerViewSlot import *
from practice.common.Container import *


class ApplicationBootstrp(QMainWindow, ControllerViewSlot):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 窗口打开时加载账号信息
        self.showAccount()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    boostrap = ApplicationBootstrp()
    boostrap.show()
    # 将ControllerViewSlot放到container中
    BeanDefinitionMap.set("ApplicationBootstrp", boostrap)
    BeanDefinitionMap.set("QApplication", app)
    sys.exit(app.exec_())
