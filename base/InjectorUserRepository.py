class Repository:
    def __init__(self, name):
        print('init...')
        self.name = name

    def sayHello(self):
        # 获取用户数据的方法
        print(f"ok：{self.name}")
