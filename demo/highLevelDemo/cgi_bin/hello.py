#!"D:\Program Files\Python313\python.exe"
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html;charset=utf-8\r\n")
print("""<html>
<head>
<meta charset="utf-8">
<title>Hello World - 我的第一个 CGI 程序</title>
</head>
<body>
<h2>Hello Python3 CGI on Windows！中文正常！</h2>
</body>
</html>""")