#!/usr/bin/python3
 
# 第一个注释
print ("Hello, Python!") # 第二个注释

# 多行注释可以用多个 # 号，还有 ''' 和 """：

'''
多行注释
萨达
擦撒大
'''

"""
这也是多行注释
adsdaaadsadsa
adsasddaas
"""

# 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print("True")
else:
    print("False")

# 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
# 实例
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#   print ("False")    # 缩进不一致，会导致运行错误

# 以上程序由于缩进不一致，执行后会出现类似以下错误：

#  File "test.py", line 6
#     print ("False")    # 缩进不一致，会导致运行错误
#                                       ^
# IndentationError: unindent does not match any outer indentation level

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：

# total = item_one + \
#         item_two + \
#         item_three
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

print(total) # 输出为 6

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：

# total = ['item_one', 'item_two', 'item_three',
#         'item_four', 'item_five']

strs = ['hello',"world","python3"]
print(strs)

# 数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j

# 字符串(String)
# Python 中单引号 ' 和双引号 " 使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \。
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
# 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
str = '123456789'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str * 2)
print(str + '您好')

print('-------------------')

print('hello\ntest')
print(r'hello\ntest')

# 以上实例输出结果：
# 123456789
# 12345678
# 1
# 345
# 3456789
# 24
# 123456789123456789
# 123456789您好
# -------------------
# hello
# test
# hello\ntest
