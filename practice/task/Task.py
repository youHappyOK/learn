import threading
import time

from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import Qt
from xiaopyDesktop import *

from practice.common.LogUtil import LogUtil
from practice.resource.desc import *
from practice.gameProcess.gameProcess import *
from practice.common.Container import *
from practice.slot.TableWidgetRereshSig import TableWidgetRereshSig
from practice.slot.TextEditRereshSig import TextEditRereshSig


class Task:

    def processTask(self, threadDict: dict, threadIndex, path):
        # 初始化线程pygame对象
        tdPy = XiaoPy()
        # 初始化线程大漠对象
        tdDm = tdPy.td_init(threadIndex)
        # 设置大漠对象
        tdPy.set_win(tdDm)
        # 方便外面解绑
        threadDict['tdDm'] = tdDm
        threadDict['threadIdent'] = threading.currentThread().ident
        tdPy.set_level(0)
        threadDict['process'] = '枚举窗口'
        self.setTableWidgetProcessItem(threadIndex, '枚举窗口')
        gameProcess = GameProcess()
        # 放置未绑定的句柄
        unbindHwnds = []
        # 状态初始值
        # 判断stopFlag是否设置标志位，设置了就正常运行，没设置直接结束
        while threadDict['stopFlag'].isSet():
            # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            threadDict['pauseFlag'].wait()
            print('线程: %s 运行中...' % threading.currentThread().ident)
            LogUtil.setTextEditLog('线程: %s 运行中...' % threading.currentThread().ident)
            if threadDict['process'] == '枚举窗口':
                hwnds = tdDm.EnumWindow(0, 'TheRender', 'RenderWindow', 1 + 2)
                # 将未绑定的句柄放到unbindHwnds中
                if hwnds != '':
                    for hwnd in hwnds.split(','):
                        hwnd = int(hwnd)
                        ret = tdDm.IsBind(hwnd)
                        if ret:
                            continue
                        print('枚举窗口 hwnd: %s 成功' % hwnd)
                        LogUtil.setTextEditLog('枚举窗口 hwnd: %s 成功' % hwnd)
                        unbindHwnds.append(hwnd)
                else:
                    LogUtil.setTextEditLog('线程: %s 未检测到模拟器...' % threading.currentThread().ident)
                    return
                print('未绑定的窗口 %s' % unbindHwnds)
                LogUtil.setTextEditLog('未绑定的窗口 %s' % unbindHwnds)
                # 设置资源文件路径
                tdPy.set_path(path)
                # 设置字典文件
                tdPy.set_dict(0, 'font.txt')
                threadDict['process'] = '绑定窗口'
                self.setTableWidgetProcessItem(threadIndex, '绑定窗口')
            elif threadDict['process'] == '绑定窗口':
                if unbindHwnds:
                    hwnd = unbindHwnds[0]
                    tdDm.BindWindow(hwnd, 'gdi', 'windows', 'windows', 0)
                    # 回写线程绑定的句柄
                    threadDict['hwnd'] = hwnd
                    tdPy.set_hwnd(hwnd)
                    print('线程: %s 绑定窗口 hwnd: %s 成功' % (threading.currentThread().ident, threadDict['hwnd']))
                    LogUtil.setTextEditLog('线程: %s 绑定窗口 hwnd: %s 成功' % (threading.currentThread().ident, threadDict['hwnd']))
                    threadDict['process'] = '打开游戏'
                    self.setTableWidgetProcessItem(threadIndex, '打开游戏')
                else:
                    print('线程: %s 绑定窗口 hwnd: %s 失败' % (threading.currentThread().ident, threadDict['hwnd']))
                    LogUtil.setTextEditLog(
                        '线程: %s 绑定窗口 hwnd: %s 失败' % (threading.currentThread().ident, threadDict['hwnd']))
            elif threadDict['process'] == '打开游戏':
                tdPy.run_action(Action().click(Point(1097, 268)))
                threadDict['process'] = '账号登录'
                print('打开游戏成功')
                LogUtil.setTextEditLog('打开游戏成功')
                self.setTableWidgetProcessItem(threadIndex, '账号登录')
            elif threadDict['process'] == '账号登录':
                accountName = threadDict['accountInfo'].split('|')[0]
                pwd = threadDict['accountInfo'].split('|')[1]
                task = [
                    Action(desc['wechat']).sleep(1).click(Point(1054, 417)).sleep(1).input('#c#' + accountName).sleep(1)
                    .click(Point(1072, 498)).input('#c#' + pwd).sleep(1).s(1).cs(2),
                    # 记得将状态机状态还原
                    Action(desc['readAgreement']).func(lambda: print('已阅读')).sleep(1).click(Point(1022, 624)).after('退出')
                    .s(2).cs(None),
                    Action(desc['wechat']).func(lambda: print('未阅读')).click(Point(766, 560)).sleep(1).click(Point(1022, 624)).s(3).cs(None).after('退出'),
                ]
                # 设置状态机，先后顺序必须状态机
                tdPy.cs(1).run(task)
                print('账号登录成功')
                LogUtil.setTextEditLog('账号登录成功')
                threadDict['process'] = '选择区服'
                self.setTableWidgetProcessItem(threadIndex, '选择区服')
            elif threadDict['process'] == '选择区服':
                task = [
                    Action(desc['enterGame']).func(lambda: print("找到进入游戏")).sleep(3).click(Point(1142, 693)).after('退出')
                ]
                tdPy.run(task)
                print('选择区服成功')
                LogUtil.setTextEditLog('选择区服成功')
                threadDict['process'] = '角色选择'
                self.setTableWidgetProcessItem(threadIndex, '角色选择')
            elif threadDict['process'] == '角色选择':
                task = [
                    Action(desc['角色选择大']).func(lambda: print("找到吉姆哥大")).click(Point(630, 387)).sleep(2),
                    Action(desc['角色选择小']).func(lambda: print("找到吉姆哥小")).click(Point(541, 524)).sleep(2).after('退出')
                ]
                tdPy.run(task)
                print('角色选择完成')
                LogUtil.setTextEditLog('角色选择完成')
                threadDict['process'] = '进入游戏'
                self.setTableWidgetProcessItem(threadIndex, '进入游戏')
            elif threadDict['process'] == '进入游戏':
                print('进入游戏')
                LogUtil.setTextEditLog('进入游戏')
                threadDict['process'] = '游戏操作'
                self.setTableWidgetProcessItem(threadIndex, '游戏操作')
            elif threadDict['process'] == '游戏操作':
                print('游戏操作')
                LogUtil.setTextEditLog('游戏操作')
                gameProcess.gameOpration(threadDict)
                threadDict['process'] = '任务完成'
            elif threadDict['process'] == '任务完成':
                print('任务完成')
                LogUtil.setTextEditLog('任务完成')
                threadDict['process'] = '任务完成'
            time.sleep(2)

    def setTableWidgetProcessItem(self, row: int, process: str):
        print('更新tableWidget' + process)
        bootStrap = BeanDefinitionMap.get("ApplicationBootstrp")
        # 这里必须通过pytqt事件才能刷新前台页面
        # 创建信号
        tableWidgetRereshSig = TableWidgetRereshSig()
        # 连接槽函数
        tableWidgetRereshSig.tableWidgetRereshSig.connect(bootStrap.tableWidgetHandleSignal)
        # 发射信号
        tableWidgetRereshSig.tableWidgetRereshSig.emit(row, process)



