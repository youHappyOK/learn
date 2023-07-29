import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
# Match对象可以用if语句进行条件判断，因为它实现了特殊方法__bool__()，也就是布尔值转换方法。
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切分字符串
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
用编译后的正则表达式去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com
'''
def is_valid_email(addr):
    if re.match(r'^([0-9a-zA-Z\.]+)\@([0-9a-zA-Z]+)\.com$', addr):
        return True
    else:
        return False
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
print('--------------------------------------------')

'''
版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
'''

def name_of_email(addr):
    matchRet = re.match(r'^\<?(\w*\s*\w*)\>?\s*?(\w*)?\@\w+\.\w+$', addr)
    print(matchRet.groups())
    if matchRet:
        return matchRet.groups(1)[0]
    else:
        return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

