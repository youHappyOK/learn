import threading
import time
from PyQt5.QtCore import QTimer


class ThreadProcess:

    def __init__(self):
        self.threadGroup = []

    def runProcessThread(self):
        threadObj = threading.Thread(target=self.runFuc, args=(0,), name='mainThread')
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

    def runFuc(self, threadIndex):
        threadDict = self.threadGroup[threadIndex]
        # 判断stopFlag是否设置标志位，设置了就正常运行，没设置直接结束
        while threadDict['stopFlag'].isSet():
            threadDict['pauseFlag'].wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print('线程: %s 运行中...' % threading.currentThread().ident)
            time.sleep(2)

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
