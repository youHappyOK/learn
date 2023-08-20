import threading
import time
from xiaopyDesktop import *

class Task:

    @staticmethod
    def processTask(threadDict: dict, threadIndex, threadLocal: threading.local):
        # todo 具体逻辑
        # 初始化线程pygame对象
        tdPy = XiaoPy()
        # 初始化线程大漠对象
        tdDm = tdPy.td_init(threadIndex)
        # 设置大漠对象
        tdPy.set_win(tdDm)
        # 设置字典文件
        # tdPy.set_dict()
        threadLocal.process = '枚举窗口'
        # 状态初始值
        # 判断stopFlag是否设置标志位，设置了就正常运行，没设置直接结束
        while threadDict['stopFlag'].isSet():
            # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            threadDict['pauseFlag'].wait()
            print('线程: %s 运行中...' % threading.currentThread().ident)
            if threadLocal.process == '枚举窗口':
                # todo，先支持一个雷电窗口的场景
                hwnd = tdDm.EnumWindow(0, 'TheRender', 'RenderWindow', 1 + 2)
                threadLocal.hwnd = int(hwnd)
                tdPy.set_hwnd(hwnd)
                print('枚举窗口 hwnd: %s 成功' % hwnd)
                threadLocal.process = '绑定窗口'
            elif threadLocal.process == '绑定窗口':
                tdDm.BindWindow(threadLocal.hwnd, 'gdi', 'windows', 'windows', 0)
                print('绑定窗口 hwnd: %s 成功' % threadLocal.hwnd)
                threadLocal.process = '绑定窗口'
            elif threadLocal.process == '打开游戏':
                print('打开游戏')
                threadLocal.process = '账号登录'
            elif threadLocal.process == '账号登录':
                print('账号登录')
                threadLocal.process = '选择区服'
            elif threadLocal.process == '选择区服':
                print('选择区服')
                threadLocal.process = '角色选择'
            elif threadLocal.process == '角色选择':
                print('角色选择')
                threadLocal.process = '进入游戏'
            elif threadLocal.process == '进入游戏':
                print('进入游戏')
                threadLocal.process = '游戏操作'
            elif threadLocal.process == '游戏操作':
                print('游戏操作')
                threadLocal.process = '任务完成'
            elif threadLocal.process == '任务完成':
                print('任务完成')
                threadLocal.process = '任务完成'
            time.sleep(2)
