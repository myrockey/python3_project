#!"D:\Program Files\Python313\python.exe"
# -*- coding: utf-8 -*-
import sys, io, os, urllib.parse, http.cookies

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-type: text/html;charset=utf-8\r\n")
print("""<html>
<head><meta charset="utf-8"><title>读取 cookie</title></head>
<body>
<h1>读取 cookie 信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie = http.cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
    if 'name' in cookie:
        raw = cookie['name'].value          # %E8%8F%9C...
        chinese = urllib.parse.unquote(raw) # 中文
        print(f"<p>cookie data: {chinese}</p>")
    else:
        print("<p>cookie 没有设置或者已过期</p>")
else:
    print("<p>HTTP_COOKIE 不存在</p>")

print("</body></html>")