import configparser
import os


class IniFileRepository:
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

