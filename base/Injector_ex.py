import injector

# 定义一个依赖注入的类
class Database:
    def __init__(self, db_name):
        print('init...')
        self.db_name = db_name

    def connect(self):
        print(f"连接到数据库：{self.db_name}")


class MyClass:
    # 使用注解标记依赖项
    @injector.inject
    def __init__(self, database: Database):
        self.database = database

    def do_something(self):
        self.database.connect()
        # 执行其他操作

class MyClass2:
    # 使用注解标记依赖项
    @injector.inject
    def __init__(self, database: Database):
        self.database = database

    def do_something(self):
        self.database.connect()
        # 执行其他操作


if __name__ == "__main__":
    # 创建一个注入器实例
    injector_instance = injector.Injector()

    # 注册依赖项
    injector_instance.binder.bind(Database, to=Database("MyDB"))

    # 通过注入器实例创建MyClass的实例
    my_class_instance = injector_instance.get(MyClass)
    my_class_instance2 = injector_instance.get(MyClass2)

    # 调用方法，该方法依赖于注入的依赖项
    my_class_instance.do_something()
    my_class_instance2.do_something()

