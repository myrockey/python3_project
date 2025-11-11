#!/usr/bin/python3

import urllib.error
import urllib.parse
import urllib.request

# 读取 url地址,整个网页内容
def get_url(url):
    res = urllib.request.urlopen(url)
    # print(res.read()) # 读取整个网页内容
    # print(res.read(300)) # 读取长度300
    # print(res.readline()) # 读取1行内容
    lines = res.readlines() # 读取多行
    for line in lines:
        print(line)

# get_url("https://www.runoob.com/")

def get_url_not_found(url):
    try:
        res = urllib.request.urlopen(url)
        print(res.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(404)

# get_url_not_found("https://www.runoob.com/no.html")

def url_save_file(url):
    res = urllib.request.urlopen(url)
    f = open("./demo/highLevelDemo/urllib_demo/urllib_test.html",'wb')
    content = res.read() # 读取网页内容
    f.write(content)
    f.close()

# url_save_file("https://www.runoob.com/")
# url编码转义
def url_encode(url):
    return urllib.request.quote(url)
# url解码
def url_decode(url):
    return urllib.request.unquote(url)

# print(url_encode("https://www.runoob.com/")) # https%3A//www.runoob.com/
# print(url_decode(url_encode("https://www.runoob.com/"))) # https://www.runoob.com/

# 模拟头部信息
def mock_url_get(url):
    keyword = 'Python 教程'
    key_code = urllib.request.quote(keyword) # 对请求进行编码
    url_all = url + key_code
    header = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }   #头部信息
    request = urllib.request.Request(url_all,headers=header)
    response = urllib.request.urlopen(request).read()

    fh = open("./demo/highLevelDemo/urllib_demo/urllib_test_runoob_search.html",'wb') # 将写入当前目录的文件
    fh.write(response)
    fh.close()

# mock_url('https://www.runoob.com/?s=')

# 表单 POST 传递数据，我们先创建一个表单，代码如下，我这里使用了 PHP 代码来获取表单的数据：
'''

'''
def mock_url_post(url):
    data = {'name':'runoob','tag':'菜鸟教程'} # 提交数据
    header = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}   #头部信息
    data = urllib.parse.urlencode(data).encode('utf8') # 对参数进行编码，解密是呀urllib.parse.urldecode
    request = urllib.request.Request(url,data,header) # 请求处理
    response = urllib.request.urlopen(request).read() # 读取结果
    
    fh = open("./demo/highLevelDemo/urllib_demo/urllib_test_runoob_post.html",'wb') # 将写入当前目录的文件
    fh.write(response)
    fh.close()

# mock_url_post('http://localhost/py3_urllib_test.php')


"""执行以上代码，会提交表单数据到 py3_urllib_test.php 文件，输出结果写入到 urllib_test_post_runoob.html 文件。

打开 urllib_test_post_runoob.html 文件（可以使用浏览器打开），显示结果如下：
"""

# urllib.parse
'''
urllib.parse 用于解析 URL，格式如下：

urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
urlstring 为 字符串的 url 地址，scheme 为协议类型，

allow_fragments 参数为 false，则无法识别片段标识符。相反，它们被解析为路径，参数或查询组件的一部分，并 fragment 在返回值中设置为空字符串。
'''
def url_parse(url):
    return urllib.parse.urlparse(url)

o = url_parse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o) # ParseResult(scheme='https', netloc='www.runoob.com', path='/', params='', query='s=python+%E6%95%99%E7%A8%8B', fragment='')
print(o.scheme,o.netloc) # https www.runoob.com

'''
从结果可以看出，内容是一个元组，包含 6 个字符串：协议，位置，路径，参数，查询，判断。

我们可以直接读取协议内容：

完整内容如下：

属性

索引

值

值（如果不存在）

scheme

0

URL协议

scheme 参数

netloc

1

网络位置部分

空字符串

path

2

分层路径

空字符串

params

3

最后路径元素的参数

空字符串

query

4

查询组件

空字符串

fragment

5

片段识别

空字符串

username

用户名

None

password

密码

None

hostname

主机名（小写）

None

port

端口号为整数（如果存在）

None
'''

# urllib.robotparser
def url_robotparser(url):
    import urllib.robotparser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url.strip())          # 去掉多余空格
    rp.read()

    rrate = rp.request_rate("*")
    # 1. 没有定义 request-rate → 对象无属性
    if rrate is None or not hasattr(rrate, 'requests'):
        print('站点未提供 Request-rate 字段')
        rrate = None
    else:
        print('Request-rate: ', rrate.requests, '次 /', rrate.seconds, '秒')

    print('Crawl-delay: ', rp.crawl_delay("*"))
    print('Can fetch search? ', rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
    print('Can fetch root? ', rp.can_fetch("*", "http://www.musi-cal.com/"))

# 测试
url_robotparser("http://www.musi-cal.com/robots.txt")
'''
结果：
站点未提供 Request-rate 字段
Crawl-delay:  None
Can fetch search?  True
Can fetch root?  True
'''

'''
urllib.robotparser
urllib.robotparser 用于解析 robots.txt 文件。

robots.txt（统一小写）是一种存放于网站根目录下的 robots 协议，它通常用于告诉搜索引擎对网站的抓取规则。

urllib.robotparser 提供了 RobotFileParser 类，语法如下：

class urllib.robotparser.RobotFileParser(url='')
这个类提供了一些可以读取、解析 robots.txt 文件的方法：

set_url(url) - 设置 robots.txt 文件的 URL。

read() - 读取 robots.txt URL 并将其输入解析器。

parse(lines) - 解析行参数。

can_fetch(useragent, url) - 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。

mtime() -返回最近一次获取 robots.txt 文件的时间。 这适用于需要定期检查 robots.txt 文件更新情况的长时间运行的网页爬虫。

modified() - 将最近一次获取 robots.txt 文件的时间设置为当前时间。

crawl_delay(useragent) -为指定的 useragent 从 robots.txt 返回 Crawl-delay 形参。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。

request_rate(useragent) -以 named tuple RequestRate(requests, seconds) 的形式从 robots.txt 返回 Request-rate 形参的内容。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。

site_maps() - 以 list() 的形式从 robots.txt 返回 Sitemap 形参的内容。 如果此形参不存在或者此形参的 robots.txt 条目存在语法错误，则返回 None。
'''
