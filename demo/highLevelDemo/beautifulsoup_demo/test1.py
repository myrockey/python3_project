#!/usr/bin/python3

def test():
    from bs4 import BeautifulSoup
    import requests

    # 使用 requests 获取网页内容
    url = 'https://cn.bing.com/' # 抓取bing搜索引擎的网页内容
    response = requests.get(url)

    # 使用 BeautifulSoup 解析网页
    soup = BeautifulSoup(response.text, 'lxml')  # 使用 lxml 解析器
    # 解析网页内容 html.parser 解析器
    # soup = BeautifulSoup(response.text, 'html.parser')

def get_html():
    from bs4 import BeautifulSoup
    import requests

    # 指定你想要获取标题的网站
    url = 'https://cn.bing.com/' # 抓取bing搜索引擎的网页内容

    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 中文乱码问题
    response.encoding = 'utf-8' 
    # 确保请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 查找<title>标签
        title_tag = soup.find('title')
        
        # 打印标题文本
        if title_tag:
            print(title_tag.get_text())
        else:
            print("未找到<title>标签")
    else:
        print("请求失败，状态码：", response.status_code)

# get_html()

# 中文乱码问题
def get_html_encoding():
    import requests

    url = 'https://cn.bing.com/'
    response = requests.get(url)

    # 使用 chardet 自动检测编码
    import chardet # 找不到时，请安装 pip install chardet
    encoding = chardet.detect(response.content)['encoding']
    print(encoding)
    response.encoding = encoding

# get_html_encoding()

# 查找标签
def get_html_tag():
    from bs4 import BeautifulSoup
    import requests

    # 指定你想要获取标题的网站
    url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容

    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 中文乱码问题
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    # 查找第一个 <a> 标签
    first_link = soup.find('a')
    print(first_link)
    print("----------------------------")

    # 获取第一个 <a> 标签的 href 属性
    first_link_url = first_link.get('href')
    print(first_link_url)
    print("----------------------------")

    # 查找所有 <a> 标签
    all_links = soup.find_all('a')
    print(all_links)

# get_html_tag()

# 获取标签的文本
def get_html_tag_text():
    from bs4 import BeautifulSoup
    import requests

    # 指定你想要获取标题的网站
    url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容

    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 中文乱码问题
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    # 获取第一个 <p> 标签中的文本内容
    paragraph_text = soup.find('p').get_text()
    # print(paragraph_text)
    # 获取页面中所有文本内容
    all_text = soup.get_text()
    print(all_text)

# get_html_tag_text()

# 查找子标签和父标签
def get_parent_child_tag():
    from bs4 import BeautifulSoup
    import requests

    # 指定你想要获取标题的网站
    url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容

    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 中文乱码问题
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    # 查找第一个 <a> 标签
    first_link = soup.find('a')
    print(first_link)
    print("----------------------------")

    # 获取当前标签的父标签
    parent_tag = first_link.parent
    print(parent_tag.get_text())

# get_parent_child_tag()

# 查找具有特定属性的标签
def get_special_tag():
    from bs4 import BeautifulSoup
    import requests

    # 指定你想要获取标题的网站
    url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容

    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 中文乱码问题
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    # 查找具有 id="unique-id" 的 <input> 标签
    unique_input = soup.find('input', id='su')

    input_value = unique_input['value'] # 获取 input 输入框的值

    print(input_value)

# get_special_tag()

'''
高级用法
CSS 选择器
BeautifulSoup 也支持通过 CSS 选择器来查找标签。

select() 方法允许使用类似 jQuery 的选择器语法来查找标签：

# 使用 CSS 选择器查找所有 class 为 'example' 的 <div> 标签
example_divs = soup.select('div.example')

# 查找所有 <a> 标签中的 href 属性
links = soup.select('a[href]')
处理嵌套标签
BeautifulSoup 支持深度嵌套的 HTML 结构，你可以通过递归查找子标签来处理这些结构：

# 查找嵌套的 <div> 标签
nested_divs = soup.find_all('div', class_='nested')
for div in nested_divs:
    print(div.get_text())


修改网页内容
BeautifulSoup 允许你修改 HTML 内容。

我们可以修改标签的属性、文本或删除标签：

实例
# 修改第一个 <a> 标签的 href 属性
first_link['href'] = 'http://new-url.com'

# 修改第一个 <p> 标签的文本内容
first_paragraph = soup.find('p')
first_paragraph.string = 'Updated content'

# 删除某个标签
first_paragraph.decompose()
转换为字符串
你可以将解析的 BeautifulSoup 对象转换回 HTML 字符串：

# 转换为字符串
html_str = str(soup)
'''


    
