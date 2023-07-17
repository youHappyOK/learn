map1 = {'k1': 'v1', 'k2': 'v2'}
print(map1['k1'])
# print(map1['k11'])
print('k11' in map1)
print(map1.get('k11', -1))
# 删除k1 v1
map1.pop('k1')
print(map1)

# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
s.add(3)
s.add(4)
print(s)
s.remove(4)
print(s)
s2 = set([3, 5, 6])
print('s & s2: {0}, s | s2: {1}'.format(s & s2, s | s2))
