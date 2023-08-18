def trim(s):
    while len(s) > 0:
        if s[0] == ' ':
            s = s[1:]
        else:
            break
    while len(s) > 0:
        if s[-1] == ' ':
            s = s[0: -1]
        else:
            break
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')