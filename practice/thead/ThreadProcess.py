import threading
import time
from PyQt5.QtCore import QTimer
from practice.task.Task import *


class ThreadProcess:

    def __init__(self):
        self.threadGroup = []
        self.threadLocal = threading.local()

    # 启动threadNum个线程
    def runProcessThread(self, threadNum):
        print('启动 %s 个线程...' % threadNum)
        for i in range(threadNum):
            threadObj = threading.Thread(target=self.runFuc, args=(i, self.threadLocal), name='mainThread')
            pauseFlag = threading.Event()  # 用于暂停线程的标识
            pauseFlag.set()  # 设置为True
            stopFlag = threading.Event()  # 用于停止线程的标识
            stopFlag.set()  # 将runningFlag设置为True
            threadDict = {'threadObj': threadObj, 'pauseFlag': pauseFlag, 'stopFlag': stopFlag}
            # 加入线程组
            self.threadGroup.append(threadDict)
        # 启动线程组
        for threadInfo in self.threadGroup:
            threadInfo.get('threadObj').start()

    def runFuc(self, threadIndex, threadLocal):
        Task.processTask(self.threadGroup[threadIndex], threadIndex, self.threadLocal)


    # 暂定指定序号的线程
    def pauseProcessThread(self, threadIndex):
        self.threadGroup[threadIndex]['pauseFlag'].clear()

    # 恢复指定序号的线程
    def resumeProcessThread(self, threadIndex):
        self.threadGroup[threadIndex]['pauseFlag'].set()

    # 结束指定序号的线程
    def stopProcessThread(self, threadIndex):
        self.threadGroup[threadIndex]['stopFlag'].clear()
        self.threadGroup[threadIndex]['pauseFlag'].set()
