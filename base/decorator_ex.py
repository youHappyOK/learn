import functools
import time


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()

print(now.__name__)


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('execute')
def now2():
    print('2015-3-25')


now2()

print(now2.__name__)


# 练习 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        startMillis = int(round(time.time() * 1000))
        ret = fn(*args, **kw)
        endMillis = int(round(time.time() * 1000))
        print('%s executed in %s ms' % (fn.__name__, endMillis - startMillis))
        return ret

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

def log(args0):
    def decorate(func):
        def wrapper(*args1, **kw):
            if args0 != None:
                print('%s %s() %s:' % (args0, func.__name__, 'begin call'))
                result = func(*args1, **kw)
                print('%s %s() %s:' % (args0, func.__name__, 'end call'))
                return result
            else:
                print('%s() %s:' % (func.__name__, 'begin call'))
                result = func(*args1, **kw)
                print('%s() %s:' % (func.__name__, 'end call'))
                return result
        return wrapper
    return decorate

@log(123)
def f(x, y):
    return x + y
#测试
r = f(1,2)
print(r)