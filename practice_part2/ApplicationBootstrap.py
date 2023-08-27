# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from practice_part2.common.ThreadGroup import ThreadGroup
from practice_part2.controller.ViewController import ViewController
from practice_part2.view.View import *
from practice_part2.repo.FileRepo import FileRepo
from practice_part2.process.MainProcess import MainProcess
from practice_part2.process.GameOpration import GameOpration


# ALT + C	要求给出建议（当有暗色字出现时，按tab接受建议）
# 快捷键	功能
# TAB	接受建议
# ESC	取消建议
# →	选择下一个建议
# ←	选择上一个建议

# 程序入口
class ApplicationBootstrap:

    def __init__(self):
        # 放到 ioc 容器中
        FileRepo()
        View()
        ViewController()
        ThreadGroup()
        MainProcess()
        GameOpration()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ApplicationBootstrap()
    sys.exit(app.exec_())
