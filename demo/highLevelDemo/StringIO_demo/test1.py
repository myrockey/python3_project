#!/usr/bin/python3

from io import StringIO

# 模拟文件操作
def test():
    # 创建StringIO对象
    string_io = StringIO()

    # 写入数据
    string_io.write("Python is awesome!\n")
    string_io.write("StringIO is useful!")

    # 移动指针到开头 0-开头，1-当前位置，2-末尾
    string_io.seek(0)

    # 读取数据
    print(string_io.read())

    # 关闭对象
    string_io.close()

# test()


def test2():
    # 创建一个 StringIO 对象
    string_io = StringIO()

    # 写入字符串
    string_io.write("Hello, World!\n")
    string_io.write("This is a test.")

    # 移动文件指针到开头
    string_io.seek(0)

    # 读取内容
    content = string_io.read() # 从 StringIO 对象中读取最多 size 个字符。如果未指定 size，则读取全部内容。
    print(content)

    # 获取所有内容
    value = string_io.getvalue() # 返回 StringIO 对象中的所有内容，作为一个字符串。
    print(value)

    # 关闭 StringIO 对象
    string_io.close()

test2()

'''
输出：
Hello, World!
This is a test.
Hello, World!
This is a test.
'''