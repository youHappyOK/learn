# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from practice_part2.controller.ViewController import ViewController
from practice_part2.view.View import *

# ALT + C	要求给出建议（当有暗色字出现时，按tab接受建议）
# 快捷键	功能
# TAB	接受建议
# ESC	取消建议
# →	选择下一个建议
# ←	选择上一个建议

# 程序入口
class ApplicationBootstrap:
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    View()
    ViewController()
    sys.exit(app.exec_())
