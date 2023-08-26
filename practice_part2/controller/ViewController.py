from practice_part2.controller.SlotFunc import *
from practice_part2.common.Container import *

class ViewController:

    def __init__(self):
        super().__init__()
        self.view = Container.get('View')
        self.view.show()
        Container.set('ViewController', self)
        self.eventInit()

    # ≥ı ºªØ–≈∫≈
    def eventInit(self):
        self.view.pushButton_5.clicked.connect(SlotFunc.saveSetting)
        self.view.pushButton_6.clicked.connect(SlotFunc.loadSetting)
        self.view.pushButton_7.clicked.connect(SlotFunc.loadAccount)


