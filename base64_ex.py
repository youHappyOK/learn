import base64

print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# 字节字符串中的每个字符都是一个字节，代表一个整数值（0-255范围内）。
print(base64.urlsafe_b64decode('abcd--__'))

# 请写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    n = len(s) - (len(s) // 4) * 4
    tail = ''
    for i in range(n):
        tail += '='
    return base64.urlsafe_b64decode(s + tail)
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')