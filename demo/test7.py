#!/usr/bin/python3

'''
Python3 基本数据类型
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''
counter = 100 # 整型变量
miles = 1000.0 # 浮点型变量
name = "test" # 字符串

print(counter)
print(miles)
print(name)

'''
执行结果：
100
1000.0
test
'''

'''
多个变量赋值
Python允许你同时为多个变量赋值。例如：

a = b = c = 1
以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

可以通过 type() 函数查看变量的类型：
'''
x = 10 # 整数
y = 3.14 # 浮点数
str = 'alice' # 字符串
is_active = True # 布尔值

# 多变量赋值
a,b,c = 1,2,'three'

# 查看数据类型
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(str)) # <class 'str'>
print(type(is_active)) # <class 'bool'>

'''
标准数据类型
Python3 中常见的数据类型有：

Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。

Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。

>>> a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

'''
n = 111
print(isinstance(a,int)) # True

'''
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass

class B(A):
    pass

print(isinstance(A(),A)) # True
print(type(A()) == A) # True
print(isinstance(B(),A)) # True
print(type(B()) == A) # False

'''
注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
'''
print(issubclass(bool,int)) # True
print(True == 1)  # True
print(False == 0) # True
print(True + 1) # 2
print(False + 1) # 1
print( 1 is True) # False
print( 0 is False) # False

'''
>>> 1 is True
<python-input-12>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  1 is True
False
>>> 0 is False
<python-input-13>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  0 is False
False
什么会出现 SyntaxWarning？

Python 检测到你在用 is 比较一个字面量整数（如 1）和 True，这通常是代码错误（因为 is 比较的是身份，而不是值）。

Python 建议你使用 == 来比较值是否相等，除非你确实想检查是否是同一个对象。

在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
'''

'''
当你指定一个值时，Number 对象就会被创建：

var1 = 1
var2 = 10
您也可以使用del语句删除一些对象引用。

del 语句的语法是：

del var1[, var2[, var3[...., varN]]]
您可以通过使用 del 语句删除单个或多个对象。例如：

del var
del var_a, var_b
'''
var1 = 1
var2 = 10

del var1,var2
print(var1)
'''
Traceback (most recent call last):
  File "d:\projects\python3_project\test7.py", line 155, in <module>
    print(var1)
          ^^^^
NameError: name 'var1' is not defined. Did you mean: 'vars'?
'''
