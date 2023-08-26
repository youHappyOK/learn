from practice_part2.controller.SlotFunc import *
from practice_part2.common.Container import *

class ViewController:

    def __init__(self):
        super().__init__()
        self.view = Container.get('View')
        self.view.show()
        Container.set('ViewController', self)

    # ≥ı ºªØ–≈∫≈
    def eventInit(self):
        self.view.pushButton_5.clicked.connect(SlotFunc.saveSetting)


