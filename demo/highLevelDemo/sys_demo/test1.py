#!/usr/bin/python3

import sys,os

# 列出模块os的所有属性和方法
def list_func_attr():
    return dir(os)

# print(list_func_attr())

# 命令行参数
def get_args():
    return sys.argv

# args = get_args()
# print(args[0]) # 脚本名称
# print(args[1:]) # 参数列表

'''
请求：& "D:/Program Files/Python313/python.exe" d:/projects/python3_project/demo/highLevelDemo/sys_demo/test1.py arg1 arg2

返回输出：

d:/projects/python3_project/demo/highLevelDemo/sys_demo/test1.py
['arg1', 'arg2']
'''

# 程序退出！

def exit():
    print('程序退出！')
    sys.exit(0)
    print('这行不会执行')

# exit()

# 标准输入输出
# sys.stdin、sys.stdout 和 sys.stderr 分别代表标准输入、标准输出和标准错误流。你可以重定向这些流以实现自定义的输入输出行为。
def log_output():
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/output.log', 'w',encoding='utf-8') as f:
        sys.stdout = f
        print("这行内容将写入 output.log")

# log_output()

# 恢复标准输入输出
def stdout():
    sys.stdout = sys.__stdout__
    print("这行内容将显示在控制台")

# stdout()

# python版本信息
def get_version():
    print('python 版本',sys.version)
    print('版本信息：',sys.version_info)

# get_version()
'''
python 版本 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)]
版本信息： sys.version_info(major=3, minor=13, micro=6, releaselevel='final', serial=0)
'''

# 模块搜索路径
def set_search_path(path):
    print("模块搜索路径：",sys.path)
    sys.path.append(path)
    print("更新后的模块搜索路径：",sys.path)

# set_search_path("d:/project")

