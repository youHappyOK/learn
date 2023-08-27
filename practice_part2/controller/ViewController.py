from practice_part2.controller.SlotFunc import *
from practice_part2.common.Container import *


class ViewController:

    def __init__(self):
        super().__init__()
        self.view = Container.get('View')
        self.showView()
        Container.set('ViewController', self)
        self.eventInit()

    # ������ʾ���ƣ���ע��ɹ��Ż���ʾ����
    # ʲô����ע�᣺��Ϸ�ͻ��˻�ɨ��windows��ע���ע�������д�Į�ͱ���
    # �¿��Ĭ�Ͼ�����ע���
    def showView(self):
        self.view.show()

    # ��ʼ���ź�
    def eventInit(self):
        self.view.pushButton_5.clicked.connect(SlotFunc.saveSetting)
        self.view.pushButton_6.clicked.connect(SlotFunc.loadSetting)
        self.view.pushButton_7.clicked.connect(SlotFunc.loadAccount)
        self.view.pushButton.clicked.connect(SlotFunc.start)
        self.view.pushButton_2.clicked.connect(SlotFunc.pause)
        self.view.pushButton_3.clicked.connect(SlotFunc.resume)
        self.view.pushButton_4.clicked.connect(SlotFunc.stop)
