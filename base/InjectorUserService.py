import injector
from base.InjectorUserRepository import Repository


class UserService:

    @injector.inject
    def __init__(self, repo: Repository):
        self.repo = repo

    def getUser(self):
        self.repo.sayHello()
