import threading
import time


# 继承Thread类，并重写它的run()方法
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):  # 定义每个线程要运行的函数

        print("name:%s start" % self.name)
        time.sleep(3)
        print("name:%s end" % self.name)


if __name__ == '__main__':
    t1 = MyThread('云云')
    t2 = MyThread('憨憨')
    # 设置子线程为守护线程，实现主程序结束，子程序立马全部结束功能，默认为False
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    t1.start()
    t2.start()
    # 使用join函数，主线程将被阻塞，一直等待被使用了join方法的线程运行完成
    # t1.join()
    # t2.join()