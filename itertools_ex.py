import itertools

# 它接受两个参数：start 和 step。
# start 表示起始值，即生成的整数序列的第一个值，默认为 0。
# step 表示步长，即每个相邻整数之间的差，默认为 1。
natuals = itertools.count(2)
for n in natuals:
    print(n)
    if n == 10:
        break

n = 1
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print(c)
    n += 1
    if n == 10:
        break

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


#
def pi(N):
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x: x <= 2*N-1, natuals)
    pi = 0
    count = 0
    for n in ns:
        if count >= N:
            break
        if count % 2 == 0:
            pi += 4*(1/n)
        else:
            pi -= 4*(1/n)
        count += 1
    return pi
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
