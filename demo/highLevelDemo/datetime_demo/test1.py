#!/usr/bin/python3

from datetime import datetime,timedelta,date
import pytz

print("当前时间:", datetime.now())
print('特定时间：',datetime(2025,10,1,10,30,0))
print('格式化时间：',datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("10天后的时间：",datetime.now()+ timedelta(days=10))
print("2个日期的天数差：",(date(2025,10,30) - date(2025,9,30)).days)
print("时区，上海当前时间：",datetime.now(pytz.timezone('Asia/Shanghai')))

# 时区转换
utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
beijing_time = utc_time.astimezone(pytz.timezone("Asia/Shanghai"))
print("时区转换:",beijing_time)

t = datetime.strptime("2023-05-15 15:00","%Y-%m-%d %H:%M")
print("解析字符串为时间格式：",type(t),t)

'''
输出：
当前时间: 2025-11-06 17:58:27.204060
特定时间： 2025-10-01 10:30:00
格式化时间： 2025-11-06 17:58:27
10天后的时间： 2025-11-16 17:58:27.204374
2个日期的天数差： 30
时区，上海当前时间： 2025-11-06 17:58:27.245306+08:00
d:\projects\python3_project\demo\highLevelDemo\datetime_demo\test1.py:14: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).        
  utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
时区转换: 2025-11-06 17:58:27.253088+08:00
解析字符串为时间格式： <class 'datetime.datetime'> 2023-05-15 15:00:00
'''

import re

text = "Contact: admin@example.com, support@test.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)  # 输出: ['admin@example.com', 'support@test.org']