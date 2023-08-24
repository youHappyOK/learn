from practice.repository.IniFileRepository import IniFileRepository
import os


class ReadIniFileService:

    def __init__(self, iniRepo: IniFileRepository):
        self.configParser = iniRepo.configParser

    # 加载账号
    def readAccount(self):
        accountPath = self.configParser.get('setting', '账号位置')
        retAccountInfo = []
        if os.path.exists(accountPath):
            with open(accountPath, 'r', encoding='utf8') as f:
                lines = f.readlines()
                if lines:
                    for line in lines:
                        retAccountInfo.append(line.strip('\n').split('|'))
        else:
            print('账号文件路径不存在！')
        return retAccountInfo

    def readTaskList(self) -> dict:
        retDict = dict()
        mainTaskList = self.configParser.get('setting', '主线').strip().split(',')
        sideTaskList = self.configParser.get('setting', '支线').strip().split(',')
        dailyTaskList = self.configParser.get('setting', '日常').strip().split(',')
        weeklyTaskList = self.configParser.get('setting', '日常').strip().split(',')
        retDict['mainTaskList'] = mainTaskList
        retDict['sideTaskList'] = sideTaskList
        retDict['dailyTaskList'] = dailyTaskList
        retDict['weeklyTaskList'] = weeklyTaskList
        return retDict