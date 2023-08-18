import argparse

'''
为了简化参数解析，我们可以使用内置的argparse库，定义好各个参数类型后，它能直接返回有效的参数。

假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：

host参数：表示MySQL主机名或IP，不输入则默认为localhost；
port参数：表示MySQL的端口号，int类型，不输入则默认为3306；
user参数：表示登录MySQL的用户名，必须输入；
password参数：表示登录MySQL的口令，必须输入；
gz参数：表示是否压缩备份文件，不输入则默认为False；
outfile参数：表示备份文件保存在哪，必须输入。
其中，outfile是位置参数，而其他则是类似--user root这样的“关键字”参数
'''
def main():
    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='backup', # 程序名
        description='Backup MySQL database.', # 描述
        epilog='Copyright(r), 2023' # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')


    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()

# python ./backup.py --database testdb backup.sql
# usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE outfile
# backup: error: the following arguments are required: -u/--user, -p/--password

# python ./backup.py -h

# python ./backup.py c: --host 127.0.0.1 --port 9949 -u root -p root --database ppt -gz