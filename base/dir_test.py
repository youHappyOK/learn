import os

# 操作系统类型
print(os.name)

# 详细的系统信息 windows没有
# print(os.uname())

# 环境变量
print(os.environ)

# 获取某个环境变量的值
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('..'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
print(os.path.join('/Users/luojin/PycharmProjects/learn', 'testdir'))

# 然后创建一个目录
# os.mkdir('/Users/luojin/PycharmProjects/learn/testdir')

# 删掉一个目录
# os.rmdir('/Users/luojin/PycharmProjects/learn/testdir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))

# 得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# 对文件重命名
# os.rename('test.txt', 'test.py')
# 删掉文件
# os.remove('test.py')

# 列出当前目录下的所有目录，列表生成式
print([x for x in os.listdir('..') if os.path.isdir(x)])
print([x for x in os.listdir('..') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# ls -l
print([x for x in os.listdir('..')])

def findFile(path, fileName):
    ret = []
    for x in os.listdir(path):
        allRelativePath = os.path.join(path, x)
        if os.path.isdir(allRelativePath):
            r = findFile(allRelativePath, fileName)
            if r is not None and len(r) != 0:
                ret.extend(r)
        elif os.path.isfile(allRelativePath) and fileName in os.path.splitext(x)[0]:
            ret.append(allRelativePath)
    return ret

print(findFile('..', 'pyvenv'))



