#!/usr/bin/python3

import requests

# requests 模块比 urllib 模块更简洁。

# 发送http请求
def requests_get(url):
    x = requests.get(url)
    return x
res = requests_get('https://www.runoob.com/')
# print(res.text) # 网页内容 unicode 类型数据
# print(res.status_code) # 响应状态码
# print(res.headers) # 响应头
# print(res.content) # 响应内容 以字节为单位
print(res.apparent_encoding) # 编码方式：utf-8
print(res.reason) # 响应状态描述：OK

res = requests_get('https://www.runoob.com/try/ajax/json_demo.json')
print(res.json()) # 返回json数据

def requests_get_header(url,req,headers):
    return requests.get(url,params=req,headers=headers)

kw = {'s':'python 教程'}

# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests_get_header("https://www.runoob.com/",kw,headers)
# 查看响应状态码
print (response.status_code) # 200

# 查看响应头部字符编码
print (response.encoding) # UTF-8

# 查看完整url地址
print (response.url) # https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B

# 查看响应内容，response.text 返回的是Unicode格式的数据
# print(response.text)

def requests_post(url,data):
    return requests.post(url,data=data)

res = requests_post('https://www.runoob.com/try/ajax/demo_post.php',{})
print(res.text)

def requests_post(url,params,data,headers):
    return requests.post(url, headers=headers, params=params, data=data)
headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
data = {'username': 'example', 'password': '123456'}  # 设置请求体
response = requests_post('https://www.runoob.com',params,data,headers)
print(response.status_code)
# 上述代码发送一个 POST 请求，并附加了请求头、查询参数和请求体