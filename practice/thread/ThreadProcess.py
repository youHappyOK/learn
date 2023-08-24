import time

from practice.task.Task import *


class ThreadProcess:

    def __init__(self):
        self.threadGroup = []

        # 初始化全局大漠对象
        self.dm = XiaoPy.gl_init("ly901107a81915b5c54de20f31cfa5a0a00ffad8", "lexgeeker01234567890")
        self.py = XiaoPy()
        # 设置操作对象
        self.py.set_win(self.dm)
        self.path = XiaoPy.get_path()
        print('项目路径 %s' % self.path)
        self.resourcePath = "\\".join(str(self.path).split("\\")[:-1]) + "\\" + 'resource'
        # 设置资源文件路径（图片等）
        self.py.set_path(self.resourcePath)
        print('资源文件路径 %s' % self.resourcePath)
        self.py.set_level(0)
        self.py.set_dict(0, 'font.txt')
        self.task = Task()

    def runProcessMainThread(self):
        runProcessMainThread = threading.Thread(target=self.runProcessThread, name='runProcessMainThread')
        runProcessMainThread.start()


    # 启动threadNum个线程
    def runProcessThread(self):
        bootStrap = BeanDefinitionMap.get("ApplicationBootstrp")
        # 多开数量
        threadNum = bootStrap.readIniFileService.readThreadNum()
        # 启动延迟
        readDelaySeconds = bootStrap.readIniFileService.readDelaySeconds()
        # 账号列表
        accountInfoList = bootStrap.readIniFileService.readAccountInfo()
        print('启动 %s 个线程...' % threadNum)
        for i in range(threadNum):
            threadObj = threading.Thread(target=self.runFuc, args=(i, ), name='runProcessThread')
            pauseFlag = threading.Event()  # 用于暂停线程的标识
            pauseFlag.set()  # 设置为True
            stopFlag = threading.Event()  # 用于停止线程的标识
            stopFlag.set()  # 将runningFlag设置为True
            threadDict = {'threadObj': threadObj, 'pauseFlag': pauseFlag, 'stopFlag': stopFlag, 'accountInfo': accountInfoList[i]}
            # 加入线程组
            self.threadGroup.append(threadDict)
        # 启动线程组
        for threadInfo in self.threadGroup:
            threadInfo.get('threadObj').start()
            # 这里sleep的时间太长了，必须在runProcessThread再套一个线程，不然pyqt5前台会卡死
            time.sleep(readDelaySeconds)

    def runFuc(self, threadIndex):
        self.task.processTask(self.threadGroup[threadIndex], threadIndex, self.resourcePath)


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

    # 关闭前台页面时触发
    def unbindThread(self):
        # 多开数量
        bootStrap = BeanDefinitionMap.get("ApplicationBootstrp")
        threadNum = int(bootStrap.readIniFileService.readThreadNum())
        print('解绑窗口')
        for i in range(threadNum):
            if 'tdDm' in self.threadGroup[i]:
                try:
                    print('解绑并停止线程: %s, 解绑窗口:%s 成功' % (self.threadGroup[i]['threadIdent'], self.threadGroup[i]['hwnd']))
                    self.threadGroup[i]['tdDm'].UnBindWindow()
                    self.stopProcessThread(i)
                except Exception as e:
                    print(e)
        self.dm.UnBindWindow()
