#!/usr/bin/python3

'''
在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
此处， _ 变量应被用户视为只读变量。
'''

'''
数学函数
函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	
返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。

其实准确的说是保留值将保留到离上一位更近的一端。

sqrt(x)	返回数字x的平方根。

随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

三角函数
Python包括以下三角函数：

函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度

数学常量
常量	描述
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。

'''

import random

print("从 range(100)返回1个随机数：",random.choice(range(100)))
print("从列表中【1,2,3,5,9]返回1个随机元素：",random.choice([1,2,3,5,9]))
print("从字符串中 'Runoob' 返回1个随机字符：",random.choice('Runoob'))

'''
以上实例运行后输出结果为：

从 range(100) 返回一个随机数 :  68
从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 :  2
从字符串中 'Runoob' 返回一个随机字符 :  u
'''

import string

def generate_password(length):
    # 定义密码可用字符集合
    chars = string.ascii_letters + string.digits + string.punctuation

    # 随机选择字符生成密码
    password = ''.join(random.choice(chars) for _ in range(length))

    return password
random_pwd = generate_password(6) # 输出长度为6
print(random_pwd)

'''
以上实例中 generate_password() 函数接受一个整数参数 length，表示要生成的密码长度，然后利用 Python 标准库中的 random 和 string 模块生成随机密码。string.ascii_letters 包含所有字母（大写和小写），string.digits 包含所有数字，string.punctuation 包含所有标点符号。

random.choice(chars) 会从字符集chars中随机选择一个字符，然后 join() 方法会将生成的字符拼接在一起形成密码。

以上实例运行后输出结果为：

R?u|<K
'''

'''
描述
seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。

语法
以下是 seed() 方法的语法:

import random

random.seed ( [x] )
我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。

注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
返回值
本函数没有返回值。

实例
以下展示了使用 seed(() 方法的实例：
'''
random.seed()
print("使用默认种子生成随机数：",random.random())
print("使用默认种子生成随机数：",random.random())
random.seed()
print("使用默认种子生成随机数：",random.random())
print("使用默认种子生成随机数：",random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：",random.random())
print("使用整数 10 种子生成随机数：",random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：",random.random())
print("使用整数 10 种子生成随机数：",random.random())

random.seed('hello',2)
print("使用字符串种子生成随机数：",random.random())
print("使用字符串种子生成随机数：",random.random())
random.seed('hello',2)
print("使用字符串种子生成随机数：",random.random())
print("使用字符串种子生成随机数：",random.random())

'''
执行结果：指定了seed值的，随机数返回是固定的

使用默认种子生成随机数： 0.45434910946440843
使用默认种子生成随机数： 0.49906478899455486
使用默认种子生成随机数： 0.9945538416802279
使用默认种子生成随机数： 0.48040613975754665
使用整数 10 种子生成随机数： 0.5714025946899135
使用整数 10 种子生成随机数： 0.4288890546751146
使用整数 10 种子生成随机数： 0.5714025946899135
使用整数 10 种子生成随机数： 0.4288890546751146
使用字符串种子生成随机数： 0.3537754404730722
使用字符串种子生成随机数： 0.6631985810268619
使用字符串种子生成随机数： 0.3537754404730722
使用字符串种子生成随机数： 0.6631985810268619
'''

'''
shuffle() 方法将序列的所有元素随机排序。

语法
以下是 shuffle() 方法的语法:

import random
 
random.shuffle (lst )
注意：shuffle() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
lst -- 列表。
返回值
返回 None。

实例
以下展示了使用 shuffle() 方法的实例：
'''
lst = [20,16,18,5]
random.shuffle(lst)
print("随机排序列表：",lst)
random.shuffle(lst)
print("随机排序列表：",lst)

'''
执行结果：

随机排序列表： [18, 16, 5, 20]
随机排序列表： [20, 16, 5, 18]
'''

'''
描述
uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。

语法
以下是 uniform() 方法的语法:

import random

random.uniform(x, y)
注意：uniform()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
x -- 随机数的最小值，包含该值。
y -- 随机数的最大值，包含该值。
返回值
返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。

实例
以下展示了使用 uniform() 方法的实例：
'''
print("uniform(5,10)的随机浮点数：",random.uniform(5,10))
print("uniform(7,14)的随机浮点数：",random.uniform(7,14))
