# linux
# fpath = '/etc/timezone'

#macos
fpath = '/Users/luojin/Desktop/auvpn'

str = ''
with open(fpath, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        str += line.strip()  # 把末尾的'\n'删掉

print(str)