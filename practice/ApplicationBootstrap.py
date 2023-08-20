import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from slot.ControllerViewSlot import *


class ApplicationBootstrp(QMainWindow, ControllerViewSlot):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 窗口打开时加载账号信息
        self.showAccount()

        # 初始化全局大漠对象
        dm = XiaoPy.gl_init("ly901107a81915b5c54de20f31cfa5a0a00ffad8", "lexgeeker01234567890")
        py = XiaoPy()
        # 设置操作对象
        py.set_win(dm)
        path = XiaoPy.get_path()
        print('项目路径 %s' % path)
        # 设置资源文件路径（图片等）
        py.set_path(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    boostrap = ApplicationBootstrp()
    boostrap.show()
    sys.exit(app.exec_())
