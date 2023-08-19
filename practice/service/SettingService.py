from practice.repository.IniFileRepository import IniFileRepository


class SettingService(IniFileRepository):

    def __init__(self):
        super().__init__()
        '''
        基本设置读取
        '''
        # 程序位置
        self.progressPath = ''
        # 账号位置
        self.accountPath = ''
        # 多开数量
        self.runNum = '0'
        # 启动延迟
        self.delayNum = '0'

        '''
        游戏设置读取
        '''
        # 主线
        self.mainTask = ''
        # 支线
        self.sideTask = ''
        # 日常
        self.dailyTask = ''
        # 循环任务
        self.weeklyTask = '循环1-17'

    def saveSettingToFile(self):
        try:
            print('保存到文件中...')
            self.configParser.set('setting', '程序位置', self.progressPath)
            self.configParser.set('setting', '账号位置', self.accountPath)
            self.configParser.set('setting', '多开数量', self.runNum)
            self.configParser.set('setting', '启动延迟', self.delayNum)
            self.configParser.set('setting', '主线', self.mainTask)
            self.configParser.set('setting', '支线', self.sideTask)
            self.configParser.set('setting', '日常', self.dailyTask)
            self.configParser.set('setting', '循环任务', self.weeklyTask)
            with open(self.configPath, 'w', encoding="utf8") as f:
                self.configParser.write(f)
            print('保存成功！')
        except Exception as e:
            print('AttributeError:', e)

    # 读取配置并返回
    def readSetting(self):
        try:
            #
            print('读取文件配置')
            self.progressPath = self.configParser.get('setting', '程序位置')
            self.accountPath = self.configParser.get('setting', '账号位置')
            self.runNum = self.configParser.get('setting', '多开数量')
            self.delayNum = self.configParser.get('setting', '启动延迟')
            self.mainTask = self.configParser.get('setting', '主线')
            self.sideTask = self.configParser.get('setting', '支线')
            self.dailyTask = self.configParser.get('setting', '日常')
            self.weeklyTask = self.configParser.get('setting', '循环任务')
        except Exception as e:
            print('读取文件配置', e)

