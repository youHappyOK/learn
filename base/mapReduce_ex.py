from functools import reduce

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def multi(x, y):
        return x * y
    return reduce(multi, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    dot = s.find('.')
    def fn(x,y):
        if y != None:
            return x * 10 + y
        else:
            return x
    def char2int(x):
        if x != '.':
            return int(x)
        return None
    return reduce(fn, map(char2int, s))/10**dot

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

