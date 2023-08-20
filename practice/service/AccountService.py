from practice.repository.IniFileRepository import IniFileRepository
import os


class AccountService:

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
