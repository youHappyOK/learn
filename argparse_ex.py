import sys
import argparse

script_name = sys.argv[0]
print("脚本名称：", script_name)

# 当执行命令 python script.py arg1 arg2 时，arg1 和 arg2 将作为参数传递给脚本
# 这种方式能应付简单的参数，但参数稍微复杂点，比如可以使用-d复制目录，使用--filename *.py过滤文件名等，解析起来就非常麻烦
arg1 = sys.argv[1]
arg2 = sys.argv[2]
print("参数1：", arg1)
print("参数2：", arg2)

arguments = sys.argv[1:]
print("所有参数：", arguments)

