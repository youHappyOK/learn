from practice_part2.controller.SlotFunc import *
from practice_part2.common.Container import *


class ViewController:

    def __init__(self):
        super().__init__()
        self.view = Container.get('View')
        self.showView()
        Container.set('ViewController', self)
        self.eventInit()

    # 界面显示控制，免注册成功才会显示界面
    # 什么是免注册：游戏客户端会扫描windows的注册表，注册表如果有大漠就被封
    # 新框架默认就是免注册的
    def showView(self):
        self.view.show()

    # 初始化信号
    def eventInit(self):
        self.view.pushButton_5.clicked.connect(SlotFunc.saveSetting)
        self.view.pushButton_6.clicked.connect(SlotFunc.loadSetting)
        self.view.pushButton_7.clicked.connect(SlotFunc.loadAccount)
        self.view.pushButton.clicked.connect(SlotFunc.start)
        self.view.pushButton_2.clicked.connect(SlotFunc.pause)
        self.view.pushButton_3.clicked.connect(SlotFunc.resume)
        self.view.pushButton_4.clicked.connect(SlotFunc.stop)
