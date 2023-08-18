import configparser
import os


class IniFileRepository:
    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configPath = '..' + os.sep + "resource" + os.sep + "setting.ini"

