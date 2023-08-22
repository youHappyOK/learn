import injector
from base.InjectorUserRepository import Repository


class UserService2:

    @injector.inject
    def __init__(self, repo: Repository):
        self.repo = repo

    def getUser(self):
        self.repo.sayHello()
