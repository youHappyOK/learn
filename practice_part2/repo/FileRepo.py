import configparser
import os

from practice_part2.common.Container import Container


class FileRepo:

    def __init__(self):
        # 初始化ini文件句柄
        self.parentDir = os.path.dirname(os.path.dirname(__file__))
        self.configPath = os.path.join(self.parentDir, 'resource', 'setting.ini')  # 使用os.path.join来构建路径
        self.configParser = configparser.ConfigParser()

        print("Config file path:", self.configPath)  # 打印配置文件路径

        # 初始化configParser的时候必须读一下
        try:
            # 读取配置文件
            self.configParser.read(self.configPath, encoding='utf8')
            # 检查是否成功读取配置文件
            if self.configParser.sections():
                print("Sections in config:", self.configParser.sections())
            else:
                print("No sections found in config.")
        except Exception as e:
            print("Error reading config:", str(e))

        Container.set('FileRepo', self)

    # 保存设置文件
    def saveSettingToFile(self, progressPath='', ldConsolePath='', accountPath='', taskList=''):
        try:
            print('保存到文件中...')
            # 不区分大小写，不过没关系，win系统的path也不区分大小写
            self.configParser.set('setting', 'ldPath', progressPath)
            self.configParser.set('setting', 'ldConsolePath', ldConsolePath)
            self.configParser.set('setting', 'accountPath', accountPath)
            self.configParser.set('setting', 'taskList', taskList)
            with open(self.configPath, 'w', encoding="utf8") as f:
                self.configParser.write(f)
            print('保存成功！')
        except Exception as e:
            print('AttributeError:', e)

    # 加载账号
    def readAccount(self):
        accountPath = self.configParser.get('setting', 'accountPath')
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

    # 读取配置
    def readSetting(self) -> dict:
        retSetting = {}
        try:
            print('读取文件配置')
            retSetting['ldPath'] = self.configParser.get('setting', 'ldPath',  fallback='')
            retSetting['ldConsolePath'] = self.configParser.get('setting', 'ldConsolePath', fallback='')
            retSetting['accountPath'] = self.configParser.get('setting', 'accountPath', fallback='')
            retSetting['taskList'] = self.configParser.get('setting', 'taskList', fallback='')
        except Exception as e:
            print('读取文件配置报错', e)
        return retSetting
