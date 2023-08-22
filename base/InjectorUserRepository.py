class UserRepository:
    def __init__(self, dbName):
        # 初始化 UserRepository
        print(dbName, '我被初始化了')
        self.dbName = dbName

    def getUser(self):
        # 获取用户数据的方法
        return '123'
