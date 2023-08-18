from io import StringIO
from io import BytesIO

f = StringIO()
f.write('常温常压超导材料')
print(f.getvalue())

f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s)

f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read())