import injector
from InjectorUserRepository import UserRepository


class UserService2:

    @injector.inject
    def __init__(self, userRepo: UserRepository):
        self.userRepo = userRepo

    def getUser(self, userId):
        return self.userRepo.getUser(userId)