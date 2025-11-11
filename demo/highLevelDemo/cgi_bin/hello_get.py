#!"D:\Program Files\Python313\python.exe"
# -*- coding: utf-8 -*-
import sys, io

# 强制 stdout 用 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os, urllib.parse

# 统一解析：GET 放在 QUERY_STRING，POST 放在 stdin
method = os.environ.get("REQUEST_METHOD", "GET")
if method == "POST":
    form = urllib.parse.parse_qs(sys.stdin.read())
else:
    form = urllib.parse.parse_qs(os.environ.get("QUERY_STRING", ""))

# 取字段（默认空列表时返回空字符串）
site_name = form.get("name", [""])[0]
site_url  = form.get("url",  [""])[0]

# 输出 HTML
print("Content-Type: text/html;charset=utf-8\r\n")
print(f"""<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程 CGI 测试实例</title>
</head>
<body>
<h2>{site_name} 官网：{site_url}</h2>
</body>
</html>""")