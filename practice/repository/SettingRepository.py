from practice.repository.IniFileRepository import IniFileRepository

class SettingRepository(IniFileRepository):

    def __init__(self):
        super().__init__()
        # 程序位置
        self.progressPath = ''
        # 账号位置
        self.accountPath = ''
        # 多开数量
        self.runNum = 0
        # 启动延迟
        self.delayNum = 0
        # 主线
        self.mainTask = ''



    def saveSettingToFile(self):
        print('保存到文件中')
        pass
