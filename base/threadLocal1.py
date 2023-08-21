import threading


def my_thread_func(thread_local):
    # 在线程函数中设置 Thread Local 变量
    thread_local.my_data = threading.current_thread().name


# 创建并启动多个线程，并将 Thread Local 对象作为参数传递
threads = []
for i in range(5):
    # 创建一个 Thread Local 对象
    thread_local1 = threading.local()
    thread = threading.Thread(target=my_thread_func, args=(thread_local1,))
    threadDict = {'thread': thread, 'threadLocal': thread_local1}
    threads.append(threadDict)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread['thread'].join()

# 获取每个线程的 Thread Local 变量
for thread in threads:
    print(thread['thread'], thread['thread']['threadLocal'].my_data)
