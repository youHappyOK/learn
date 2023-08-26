#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
import time

# 加载 kernel32.dll
kernel32 = ctypes.WinDLL('kernel32.dll')

# 定义线程函数
def thread_function():
    while True:
        print("Thread is running...")
        time.sleep(1)


# 定义函数类型
ThreadProc = ctypes.WINFUNCTYPE(ctypes.c_int)

# 创建函数指针
thread_func_ptr = ThreadProc(thread_function)

# 创建线程
thread_id = ctypes.c_ulong()
thread_handle = kernel32.CreateThread(
    ctypes.c_void_p(None), 0, thread_func_ptr, None, 0, ctypes.byref(thread_id)
)

print('线程开始运行5s.....')
# 让线程运行5s
time.sleep(5)


print('暂停线程5s.....')
# 暂停线程
kernel32.SuspendThread(thread_handle)
# 暂停5s
time.sleep(5)

print('恢复线程5s.....')
# 恢复线程
kernel32.ResumeThread(thread_handle)
# 恢复线程5秒后关闭
time.sleep(5)


print('结束线程.....')
# 关闭线程句柄
# 理解错了，以为kernel32.CloseHandle是关闭线程，其实是关闭线程的句柄，其实线程还存在。。
# 它主要用于释放资源而不是直接结束线程。关闭线程的句柄并不会立即结束线程的执行。线程会继续运行，直到它完成或被终止。
kernel32.CloseHandle(thread_handle)

time.sleep(5)

print('main函数结束')