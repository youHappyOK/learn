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

    # 启动threadNum个线程
    def runProcessThread(self, threadNum):
        print('启动 %s 个线程...' % threadNum)
        for i in range(threadNum):
            threadObj = threading.Thread(target=self.runFuc, args=(i, ), name='mainThread')
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

    def unbindThread(self):
        print('解绑窗口')
        self.dm.UnBindWindow()
