#!/usr/bin/python3

import markdown,os

# 读取markdown文件
exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
import markdown

# 读取 Markdown 文件
with open(exec_path + '/example.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 将 Markdown 转换为 HTML
html = markdown.markdown(markdown_text)

# 将 HTML 写入文件
with open(exec_path + '/example.html', 'w', encoding='utf-8') as file:
    file.write(html)

print("Markdown 文件已成功转换为 HTML 文件！")
