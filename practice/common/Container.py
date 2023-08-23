class BeanDefinitionMap:

    container = dict()

    def __init__(self, **kw):
        super().__init__(**kw)

    @staticmethod
    def get(key):
        try:
            return BeanDefinitionMap.container[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    @staticmethod
    def set(key, value):
        BeanDefinitionMap.container[key] = value
