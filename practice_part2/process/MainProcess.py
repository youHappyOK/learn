#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: MainProcess.py
Author: 吉姆哥
Date: 2023/8/27
Description: 用于控制并开启游戏的主流程
"""
import threading

from practice_part2.common.CustomerThread import CustomThread
from practice_part2.common.Container import Container
from practice_part2.common.DmTool import DmTool
from practice_part2.process.SubProcess import SubProcess


class MainProcess:

    def __init__(self):
        self.threadGroup = Container.get('ThreadGroup')
        Container.set('MainProcess', self)

    def runMainProcess(self):
        # 初始化全局大漠对象
        DmTool.initGlobleDmObj()
        runProcessMainThread = threading.Thread(target=self.runThread, name='runMainProcess')
        # 启动线程组，每个窗口一个线程负责
        runProcessMainThread.start()

    # 启动threadNum个子线程线程
    def runThread(self):
        fileRepo = Container.get("FileRepo")
        # 账号列表
        accountInfoList = fileRepo.readAccount()
        # 多开数量就是账号数量
        threadNum = len(accountInfoList)
        # 启动延迟(默认10秒)
        self.threadGroup.delaySecond = 10
        print('启动 %s 个线程...' % threadNum)
        for i in range(threadNum):
            threadObj = CustomThread(SubProcess.runProcess, args=(i,), name='runSubProcess')
            # threadObj = threading.Thread(target=SubProcess.runProcess, args=(i,), name='runSubProcess')
            threadDict = {'threadObj': threadObj, 'accountInfo': accountInfoList[i]}
            # 加入线程组
            self.threadGroup.addThread(threadDict)
        # 启动线程组
        self.threadGroup.startAll()

