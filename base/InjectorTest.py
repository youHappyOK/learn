import injector

from base.InjectorUserRepository import Repository
from base.InjectorUserService import UserService
from base.InjectorUserService2 import UserService2

if __name__ == "__main__":
    # 创建一个注入器实例
    injector_instance = injector.Injector()

    # 注册依赖项
    injector_instance.binder.bind(Repository, to=Repository("MyRepo"))

    # 通过注入器实例创建UserService的实例
    user_service = injector_instance.get(UserService)
    user_service2 = injector_instance.get(UserService2)

    # 调用方法，该方法依赖于注入的依赖项
    user_service.getUser()
    user_service2.getUser()

    ## 创建一个注入器实例
    # injector_instance = injector.Injector()
    #
    # # 注册依赖项
    # injector_instance.binder.bind(Database, to=Database("MyDB"))
    #
    # # 通过注入器实例创建MyClass的实例
    # my_class_instance = injector_instance.get(MyClass)
    # my_class_instance2 = injector_instance.get(MyClass2)
    #
    # # 调用方法，该方法依赖于注入的依赖项
    # my_class_instance.do_something()
    # my_class_instance2.do_something()



