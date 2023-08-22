import injector

from base.InjectorContainer import MyContainer
from base.InjectorUserService import UserService
from base.InjectorUserService2 import UserService2

container = MyContainer()
injector = injector.Injector(container)

user_service = injector.get(UserService)
user = user_service.getUser(123)
print(user)  # 输出: User: 123


user_service2 = injector.get(UserService2)
user = user_service2.getUser(123)
print(user)  # 输出: User: 123