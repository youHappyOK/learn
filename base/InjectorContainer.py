import injector

from base.InjectorUserRepository import UserRepository
from base.InjectorUserService import UserService
from base.InjectorUserService2 import UserService2


class MyContainer(injector.Module):

    def configure(self, binder):
        binder.bind(UserService)
        binder.bind(UserService2)
        binder.bind(UserRepository)