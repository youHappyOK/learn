import injector

from base.InjectorUserRepository import UserRepository
from base.InjectorUserService import UserService
from base.InjectorUserService2 import UserService2

if __name__ == "__main__":
    # 创建一个注入器实例
    injector_instance = injector.Injector()

    # 注册依赖项
    injector_instance.binder.bind(UserRepository, to=UserRepository('rep'))

    user_service = injector_instance.get(UserService)

    user_service2 = injector_instance.get(UserService2)

    user = user_service.getUser(123)
    print(user)  # 输出: User: 123

    user = user_service2.getUser(123)
    print(user)  # 输出: User: 123