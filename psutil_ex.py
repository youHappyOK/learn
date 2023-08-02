import psutil

# 获取CPU信息
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_count(logical=False)) # CPU物理核心

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions()) # 磁盘分区信息
print(psutil.disk_usage('/')) # 磁盘使用情况
print(psutil.disk_io_counters()) # 磁盘IO

# 获取网络信息
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态

# 要获取当前网络连接信息，使用net_connections()：
# print(psutil.net_connections())

# 获取进程信息
# 和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。
print(psutil.pids())  # 所有进程ID
p = psutil.Process(116) # 获取指定进程ID=3776
print(p.name()) # 进程名称
print(p.exe()) # 进程exe路径
print(p.cwd())  # 进程工作目录
print(p.cmdline())  # 进程启动的命令行
print(p.ppid())  # 父进程ID
print(p.parent())  # 父进程
print(p.children())  # 子进程列表
p.username() # 进程用户名
p.create_time() # 进程创建时间
p.terminal() # 进程终端
p.cpu_times() # 进程使用的CPU时间
p.memory_info() # 进程使用的内存
p.open_files() # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads() # 所有线程信息
p.environ() # 进程环境变量
p.terminate() # 结束进程

# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
# psutil.test()
