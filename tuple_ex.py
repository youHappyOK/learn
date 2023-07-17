# 使用圆括号创建元组
my_tuple = (1, 2, 3)
print(my_tuple)  # 输出: (1, 2, 3)

# 使用tuple()函数创建元组
another_tuple = tuple(['apple', 'banana', 'orange'])
print(another_tuple)  # 输出: ('apple', 'banana', 'orange')

my_tuple = ('apple', 'banana', 'orange')
print(my_tuple[0])      # 输出: 'apple'
print(my_tuple[-1])     # 输出: 'orange'

my_tuple = ('apple', 'banana', 'orange', 'grape', 'kiwi')
print(my_tuple[1:4])    # 输出: ('banana', 'orange', 'grape')
print(my_tuple[:3])     # 输出: ('apple', 'banana', 'orange')
print(my_tuple[2:])     # 输出: ('orange', 'grape', 'kiwi')

my_tuple = ('a', 'b', 'c', 'a', 'a')
print(len(my_tuple))              # 输出: 5
print(my_tuple.count('a'))        # 输出: 3

my_tuple = ('John', 25, 'London')
name, age, city = my_tuple
print(name)    # 输出: 'John'
print(age)     # 输出: 25
print(city)    # 输出: 'London'

my_tuple = ('apple', 'banana', 'orange')
# 以下操作会引发错误，因为元组是不可变的
# my_tuple[0] = 'kiwi'
# del my_tuple[1]

# 创建一个新的元组来修改或扩展
modified_tuple = my_tuple + ('kiwi',)
print(modified_tuple)  # 输出: ('apple', 'banana', 'orange', 'kiwi')