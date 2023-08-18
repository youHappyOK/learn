from datetime import datetime, timedelta, timezone
import re

now = datetime.now() # 获取当前datetime
print(now)

print(type(now))

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

t = 1429417200.0
print(datetime.fromtimestamp(t))

t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
print(datetime.now())
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
def to_timestamp(dt_str, tz_str):
    # timeMatch = re.match(r'^UTC([+—]\d+)\:(\d+)$', tz_str)
    timeMatch = re.match(r'^UTC([+-]\d+):(\d+)$', tz_str)
    delta = int(timeMatch.group(1))
    tz_utc_delta = timezone(timedelta(hours=delta))
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print(cday.timestamp())
    tz_dt = cday.replace(tzinfo=tz_utc_delta)
    print(tz_dt.timestamp())
    return tz_dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

# def to_timestamp(dt_str, tz_str):
#     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#     tz = re.match(r'^UTC([+-]\d+):(\d+)$', tz_str)
#     hours = int(tz.group(1))
#     minutes = int(tz.group(2)) if hours > 0 else -int(tz.group(2))
#     dt = dt.replace(tzinfo=timezone(timedelta(hours = hours, minutes = minutes)))
#     return dt.timestamp()
#
# # 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# t3 = to_timestamp('2023-7-10 07:00:00','UTC-02:30')
# assert t3 == 1688981400.0, t3
#
# print('ok')