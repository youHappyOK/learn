import math

# 调用函数
num = hex(0xFF)
print(num)


def abs(num):
    if num < 0:
        return -num
    else:
        return num


print(abs(-99))


def nop():
    pass


def test_pass(num):
    if num > 0:
        pass
    else:
        print(num)


test_pass(-100)


def test_return():
    return 1, 2, 3


x, y, z = test_return()
print("x: {0}, y:{1}, z:{2}".format(x, y, z))


def quadratic(a, b, c):
    temp = math.sqrt(b * b - 4 * a * c)
    ans1 = (-b + temp) / (2 * a)
    ans2 = (-b - temp) / (2 * a)
    return ans1, ans2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x, n):
    m = 1
    ret = x
    while m < n:
        ret = ret * x
        m = m + 1
    return ret


print(power(2, 3))


# 默认参数
def power(x, n=3):
    m = 1
    ret = x
    while m < n:
        ret = ret * x
        m = m + 1
    return ret


print(power(2))


# 可变参数，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))


# 关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数，关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person3(name, age, *, city, job):
    print(name, age, city, job)
person3('Jack', 24, city='Beijing', job='Engineer')
