import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime

print(datetime.datetime.now())

newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

one_day = datetime.datetime(2008,5,27)
newday = datetime.timedelta(days=10)
print(one_day + newday)
