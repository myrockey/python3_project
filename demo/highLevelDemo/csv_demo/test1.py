#!/usr/bin/python3

import csv,os

# 写入csv文件、
"""
代码解释：
open('output.csv', mode='w', encoding='utf-8', newline='')：以写入模式打开名为 output.csv 的文件，并指定编码为 UTF-8。newline='' 用于避免在 Windows 系统中出现空行。
csv.writer(file)：创建一个 csv.writer 对象，用于写入文件内容。
csv_writer.writerow(row)：将每一行数据写入文件。
"""
def write_csv(data):
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data.csv',mode='w',encoding='utf-8', newline='') as file:
        # 创建 csv.writer 对象
        csv_writer = csv.writer(file)
        # 写入数据
        for row in data:
            csv_writer.writerow(row)

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]
# write_csv(data)


# 读取csv文件
def read_csv():
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data.csv',mode='r',encoding='utf-8') as file:
        # 创建 csv.reader对象
        csv_reader = csv.reader(file)
        # 逐行读取数据
        for row in csv_reader:
            print(row)

# read_csv()
'''
输出：
['Name', 'Age', 'City']
['Alice', '30', 'New York']
['Bob', '25', 'Los Angeles']
'''

"""
使用字典读取和写入 CSV 文件
csv 模块还提供了 DictReader 和 DictWriter 类，它们可以将 CSV 文件的每一行解析为字典，或者将字典写入 CSV 文件。

"""
def write_dict_csv(data):
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/dict_data.csv',mode='w',encoding='utf-8', newline='') as file:
        fieldNames = []
        for fieldName in data[0]:
            fieldNames.append(fieldName)

        # 创建 csv.writer 对象
        csv_dict_writer = csv.DictWriter(file,fieldnames=fieldNames)
        # 写入表头
        csv_dict_writer.writeheader()
        # 写入数据
        for row in data:
            csv_dict_writer.writerow(row)

data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]
# write_dict_csv(data)
def read_dict_csv():
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/dict_data.csv',mode='r',encoding='utf-8') as file:
        # 创建 csv.reader对象
        csv_dict_reader = csv.DictReader(file)
        # 逐行读取数据
        for row in csv_dict_reader:
            print(row)

# read_dict_csv()
'''
输出：
{'Name': 'Alice', 'Age': '30', 'City': 'New York'}
{'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
'''
def write_csv2(data):
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data2.csv',mode='w',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # 写入多行

data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
# write_csv2(data)

# 读取csv文件
def read_csv2():
    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data2.csv',mode='r',encoding='utf-8') as file:
        # 创建 csv.reader对象
        csv_reader = csv.reader(file,delimiter=',') # delimiter=',' 是 csv.reader 的默认值。
        # 逐行读取数据
        for row in csv_reader:
            print(row)

# read_csv2()
'''
输出：
['Name', 'Age']
['Alice', '25']
['Bob', '30']
'''

# tsv文件，和 csv文件的差别，tsv是用\t制表符作为分隔符
def write_tsv():
    rows = [
        ['id', 'name', 'age'],
        [1, 'Alice', 30],
        [2, 'Bob', 25],
    ]

    # 打开csv文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    # 注册方言（也可直接用 delimiter='\t'）
    csv.register_dialect('tsv', delimiter='\t', quoting=csv.QUOTE_NONE)

    with open(exec_path + '/data.tsv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='tsv')
        writer.writerows(rows)

    print("data.tsv 已生成！")

# write_tsv()

# 读取tsv文件
def read_tsv():
    csv.register_dialect('tsv', delimiter='\t', quoting=csv.QUOTE_NONE)
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data.tsv', 'r') as file:
        reader = csv.reader(file, dialect='tsv')
        for row in reader:
            print(row)

read_tsv()
'''
输出：
['id', 'name', 'age']
['1', 'Alice', '30']
['2', 'Bob', '25']
'''