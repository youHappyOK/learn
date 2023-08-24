# -*- coding: utf-8 -*-
import time

from practice.common.Container import BeanDefinitionMap
from practice.common.LogUtil import LogUtil


class GameProcess:

    def __init__(self):
        pass

    def gameOpration(self, threadDict):
        while threadDict['stopFlag'].isSet():
            # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            threadDict['pauseFlag'].wait()
            bootStrap = BeanDefinitionMap.get("ApplicationBootstrp")
            taskDict = bootStrap.readIniFileService.readTaskList()
            mainTaskList = taskDict.get('mainTaskList')
            sideTaskList = taskDict.get('sideTaskList')
            dailyTaskList = taskDict.get('dailyTaskList')
            weeklyTaskList = taskDict.get('weeklyTaskList')
            # 主线任务
            if '主线1-17' in mainTaskList:
                LogUtil.setTextEditLog('主线1-17进行中...')
            elif '主线18-30' in mainTaskList:
                LogUtil.setTextEditLog('主线18-30进行中...')
            elif '主线31-50' in mainTaskList:
                LogUtil.setTextEditLog('主线31-50进行中...')
            time.sleep(5)
            # 支线任务
            if '支线1-17' in sideTaskList:
                LogUtil.setTextEditLog('支线11-17进行中...')
            elif '支线18-30' in sideTaskList:
                LogUtil.setTextEditLog('支线18-30进行中...')
            elif '支线31-50' in sideTaskList:
                LogUtil.setTextEditLog('支线31-50进行中...')
            time.sleep(5)
            # 日常任务
            if '日常1-17' in dailyTaskList:
                LogUtil.setTextEditLog('日常11-17进行中...')
            elif '日常18-30' in sideTaskList:
                LogUtil.setTextEditLog('日常18-30进行中...')
            elif '日常131-50' in sideTaskList:
                LogUtil.setTextEditLog('日常31-50进行中...')
            time.sleep(5)
            # 循环任务
            if '循环1-17' in weeklyTaskList:
                LogUtil.setTextEditLog('循环11-17进行中...')
            elif '循环18-30' in sideTaskList:
                LogUtil.setTextEditLog('循环18-30进行中...')
            elif '循环31-50' in sideTaskList:
                LogUtil.setTextEditLog('循环31-50进行中...')
            time.sleep(5)
