import threading
import time
from xiaopyDesktop import *
from practice.resource.desc import *

class Task:

    @staticmethod
    def processTask(threadDict: dict, threadIndex, path):
        # todo 具体逻辑
        # 初始化线程pygame对象
        tdPy = XiaoPy()
        # 初始化线程大漠对象
        tdDm = tdPy.td_init(threadIndex)
        # 设置大漠对象
        tdPy.set_win(tdDm)
        # 设置字典文件
        # tdPy.set_dict()
        threadDict['process'] = '枚举窗口'
        # 状态初始值
        # 判断stopFlag是否设置标志位，设置了就正常运行，没设置直接结束
        while threadDict['stopFlag'].isSet():
            # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            threadDict['pauseFlag'].wait()
            print('线程: %s 运行中...' % threading.currentThread().ident)
            if threadDict['process'] == '枚举窗口':
                # todo，先支持一个雷电窗口的场景
                hwnd = tdDm.EnumWindow(0, 'TheRender', 'RenderWindow', 1 + 2)
                threadDict['hwnd'] = int(hwnd)
                tdPy.set_hwnd(hwnd)
                # 设置资源文件路径
                tdPy.set_path(path)
                print('枚举窗口 hwnd: %s 成功' % hwnd)
                threadDict['process'] = '绑定窗口'
            elif threadDict['process'] == '绑定窗口':
                tdDm.BindWindow(threadDict['hwnd'], 'gdi', 'windows', 'windows', 0)
                print('绑定窗口 hwnd: %s 成功' % threadDict['hwnd'])
                threadDict['process'] = '打开游戏'
            elif threadDict['process'] == '打开游戏':
                tdPy.run_action(Action().click(Point(1097, 268)))
                threadDict['process'] = '账号登录'
                print('打开游戏成功')
            elif threadDict['process'] == '账号登录':
                task = [
                    Action(desc['wechat']).sleep(1).click(Point(1054, 417)).sleep(1).input('#c#CodeGlory').sleep(1)
                    .click(Point(1072, 498)).input('#c#lj6234466').sleep(1).s(1).cs(2),
                    Action(desc['readAgreement']).func(lambda: print('已阅读')).sleep(1).click(Point(1022, 624)).after('退出')
                    .s(2).cs(3),
                    Action(desc['wechat']).func(lambda: print('未阅读')).click(Point(766, 560)).sleep(1).click(Point(1022, 624)).s(3).cs(None).after('退出'),
                ]
                # 设置状态机，先后顺序必须状态机
                tdPy.cs(1).run(task)
                print('账号登录成功')
                threadDict['process'] = '选择区服'
            elif threadDict['process'] == '选择区服':
                print('选择区服')
                threadDict['process'] = '选择区服'
            elif threadDict['process'] == '角色选择':
                print('角色选择')
                threadDict['process'] = '进入游戏'
            elif threadDict['process'] == '进入游戏':
                print('进入游戏')
                threadDict['process'] = '游戏操作'
            elif threadDict['process'] == '游戏操作':
                print('游戏操作')
                threadDict['process'] = '任务完成'
            elif threadDict['process'] == '任务完成':
                print('任务完成')
                threadDict['process'] = '任务完成'
            time.sleep(2)
