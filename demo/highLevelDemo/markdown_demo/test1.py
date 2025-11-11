#!/usr/bin/python3

import markdown

# 定义 Markdown 文本
md_text = """
# 这是标题
这是 **加粗** 的文本。
这是 *斜体* 的文本。

- 列表项 1
- 列表项 2

[点击这里](https://www.runoob.com) 访问网站。
"""

# 转换为 HTML
html_output = markdown.markdown(md_text)

# 输出 HTML
print(html_output)

'''
输出：
<h1>这是标题</h1>
<p>这是 <strong>加粗</strong> 的文本。
这是 <em>斜体</em> 的文本。</p>
<ul>
<li>列表项 1</li>
<li>列表项 2</li>
</ul>
<p><a href="https://www.runoob.com">点击这里</a> 访问网站。</p>
'''
