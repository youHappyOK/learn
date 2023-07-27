import pickle
import json

# pickle
d = dict(name = '你吗的', age = 50, gender = '男')
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d2 = pickle.load(f)
f.close()
print(d2)

# json
d3 = dict(name='Bob', age=20, score=88)
print(json.dumps(d3))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(type(json.loads(json_str)))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))

# 偷懒，因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)