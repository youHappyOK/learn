#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: GameOpration.py
Author: 吉姆哥
Date: 2023/8/27
Description: 游戏操作
"""
import time

from practice_part2.common.Container import Container

import threading


class GameOpration:

    def __init__(self):
        Container.set('GameOpration', self)

    def gameOpration(self):
        while True:
            fileRepo = Container.get("FileRepo")
            taskList = fileRepo.readSetting()['taskList']
            # 主线任务
            if '主线' in taskList:
                print('thread: %s 主线进行中...' % threading.currentThread().ident)
            elif '师门' in taskList:
                print('thread: %s 师门进行中...' % threading.currentThread().ident)
            elif '日常_除暴' in taskList:
                print('thread: %s 日常_除暴进行中...' % threading.currentThread().ident)
            time.sleep(5)