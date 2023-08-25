# chatgpt搜：python使用ctypes模块暂停、恢复、关闭线程（macos）
# python使用win32暂停、恢复、关闭线程（windows）

import ctypes
import threading
import time

# 加载系统库 libpthread.dylib
libpthread = ctypes.CDLL('libpthread.dylib')

# 定义相关函数原型
pthread_kill = libpthread.pthread_kill

# 定义信号常量
SIGSTOP = 17
SIGCONT = 19

def loop(thread_local):
    while True:
        # 获取当前线程Id
        thread_local.tdId = threading.currentThread().ident
        print(str(thread_local.tdId) + ' 运行中...')
        time.sleep(1)

# 创建并启动多个线程，并将 Thread Local 对象作为参数传递
threads = []
for i in range(2):
    # 创建一个 Thread Local 对象
    thread_local1 = threading.local()
    thread = threading.Thread(target=loop, args=(thread_local1,))
    threadDict = {'thread': thread}
    threads.append(threadDict)
    thread.start()

time.sleep(10)

# 暂停线程
stopThreadId = threads[0].tdId
print('暂停线程: ' + str(stopThreadId))
pthread_kill(stopThreadId, SIGSTOP)

time.sleep(10)

# 恢复线程
pthread_kill(stopThreadId, SIGCONT)

# 关闭线程
pthread_kill(stopThreadId, 9)