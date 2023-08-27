#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: SubThread.py
Author: 吉姆哥
Date: 2023/8/27
Description: 每个线程的运行流程
"""
import threading
import time

from PyGameAuto32 import PyGameAuto

from practice_part2.common.DmTool import DmTool
from practice_part2.common.Container import Container


class SubProcess:

    @staticmethod
    def runProcess(threadIndex: int):
        # 初始化线程pygame对象
        tdPy = PyGameAuto()
        # 初始化线程大漠对象
        tdDm = tdPy.td_init(threadIndex)
        # 设置大漠对象
        tdPy.set_win(tdDm)
        # 设置日志级别
        tdPy.set_level(0)
        threadDict = Container.get('ThreadGroup').get(threadIndex)
        # 方便外面解绑
        threadDict['tdDm'] = tdDm
        threadDict['threadIdent'] = threading.currentThread().ident
        threadDict['process'] = '模拟器开启'
        gameOpration = Container.get('GameOpration')
        # 放置未绑定的句柄
        unbindHwnds = []
        while True:
            print('线程: %s 运行中...' % threading.currentThread().ident)
            if threadDict['process'] == '模拟器开启':
                pass
            if threadDict['process'] == '模拟器状态判断':
                pass
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
                        unbindHwnds.append(hwnd)
                else:
                    return
                print('未绑定的窗口 %s' % unbindHwnds)
                # 设置资源文件路径
                tdPy.set_path(DmTool.resourcePath)
                # 设置字典文件
                tdPy.set_dict(0, 'font.txt')
                threadDict['process'] = '绑定窗口'
            elif threadDict['process'] == '绑定窗口':
                if unbindHwnds:
                    hwnd = unbindHwnds[0]
                    tdDm.BindWindow(hwnd, 'gdi', 'windows', 'windows', 0)
                    # 回写线程绑定的句柄
                    threadDict['hwnd'] = hwnd
                    tdPy.set_hwnd(hwnd)
                    print('线程: %s 绑定窗口 hwnd: %s 成功' % (threading.currentThread().ident, threadDict['hwnd']))
                    threadDict['process'] = '打开游戏'
                else:
                    print('线程: %s 绑定窗口 hwnd: %s 失败' % (threading.currentThread().ident, threadDict['hwnd']))
            elif threadDict['process'] == '打开游戏':
                print('打开游戏成功')
            elif threadDict['process'] == '账号登录':
                accountName = threadDict['accountInfo'].split('|')[0]
                pwd = threadDict['accountInfo'].split('|')[1]
                print('账号登录成功')
                threadDict['process'] = '选择区服'
            elif threadDict['process'] == '选择区服':
                print('选择区服成功')
                threadDict['process'] = '角色选择'
            elif threadDict['process'] == '角色选择':
                print('角色选择完成')
                threadDict['process'] = '进入游戏'
            elif threadDict['process'] == '进入游戏':
                print('进入游戏')
                threadDict['process'] = '游戏操作'
            elif threadDict['process'] == '游戏操作':
                print('游戏操作')
                gameOpration.gameOpration(threadDict)
                threadDict['process'] = '任务完成'
            elif threadDict['process'] == '任务完成':
                print('任务完成')
                threadDict['process'] = '任务完成'
            time.sleep(2)