# -*- coding: utf-8 -*-

from practice.common.Container import BeanDefinitionMap
from practice.slot.TextEditRereshSig import TextEditRereshSig


class LogUtil:

    @staticmethod
    def setTextEditLog(log: str):
        print('更新tableWidget' + log)
        bootStrap = BeanDefinitionMap.get("ApplicationBootstrp")
        # 这里必须通过pytqt事件才能刷新前台页面
        # 创建信号
        textEditRereshSig = TextEditRereshSig()
        # 连接槽函数
        textEditRereshSig.textEditRereshSig.connect(bootStrap.textEditHandleSignal)
        # 发射信号
        textEditRereshSig.textEditRereshSig.emit(log)