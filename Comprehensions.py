L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if isinstance(word, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')