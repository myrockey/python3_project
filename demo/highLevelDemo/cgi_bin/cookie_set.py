#!"D:\Program Files\Python313\python.exe"
import sys, io, datetime as dt, urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. 过期时间 = 现在 + 1 小时
expire = (dt.datetime.now() + dt.timedelta(hours=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')

# 2. 对值做 URL 编码（中文+空格）
value = urllib.parse.quote('菜鸟教程')

print(f'Set-Cookie: name={value}; expires={expire}; Path=/')
print('Content-Type: text/html;charset=utf-8\r\n')

print('''
<html>
  <head>
    <meta charset="utf-8">
    <title>CGI Cookie</title>
  </head>
  <body>
    <h1>Cookie set OK!</h1>
  </body>
</html>''')