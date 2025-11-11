#!"D:\Program Files\Python313\python.exe"
# -*- coding: utf-8 -*-
import sys, io, os, re, tempfile,traceback

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    #########################
    content_len = int(os.environ.get('CONTENT_LENGTH', 0))
    raw = sys.stdin.buffer.read(content_len)

    # 1. 拿到 boundary（bytes）
    boundary = re.search(r'boundary=(.+)', os.environ.get('CONTENT_TYPE', '')).group(1).encode()

    # 2. 去掉最前面的 "--boundary\r\n" 空段
    parts = raw.split(b'--' + boundary + b'\r\n')
    if len(parts) < 2:
        message = '未找到上传数据'
    else:
        body = parts[1]                      # 第一段表单数据
        header, file_bytes = body.split(b'\r\n\r\n', 1)
        file_bytes = file_bytes.rsplit(b'\r\n', 1)[0]   # 去掉尾部换行

        fn_match = re.search(rb'filename="([^"]+)"', header)
        if fn_match:
            fn = os.path.basename(fn_match.group(1).decode('utf-8'))
            save_path = os.path.join(tempfile.gettempdir(), fn)
            with open(save_path, 'wb') as f:
                f.write(file_bytes)
            message = f'文件 "{fn}" 上传成功，保存于 {save_path}'
        else:
            message = '文件名解析失败'
    #########################
    print("Content-Type: text/html;charset=utf-8\r\n")
    print(f"<html><body><h1>上传结果：{message}</h1></body></html>")

except Exception as e:
    # 把异常打到浏览器，方便调试
    print("Content-Type: text/html;charset=utf-8\r\n")
    print("<html><body><pre>")
    traceback.print_exc(file=sys.stdout)
    print("</pre></body></html>")
