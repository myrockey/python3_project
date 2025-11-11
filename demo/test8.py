#!/usr/bin/python3

'''
数值运算
实例
>>> 5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余
2
>>> 2 ** 5 # 乘方
32
注意：

1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
'''
print(5+4 # 加法 9
      ,4.3-2 # 减法 2.3
      ,3*7 # 乘法 21
      ,2/4 # 除法，得到1个浮点数 0.5
      ,2//4 # 除法，得到1个整数 0
      ,17%3 # 取余 2
      ,2**5 # 乘方 32
      )

'''
数值类型实例
int	float	complex
10	0.0	3.14j
100	15.20	45.j
-786	-21.9	9.322e-36j
080	32.3e+18	.876j
-0490	-90.	-.6545+0J
-0x260	-32.54e100	3e+26J
0x69	70.2E-12	4.53e-7j
Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
'''

'''
String（字符串）
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

字符串的截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。



加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：

实例
#!/usr/bin/python3

str = 'Runoob'  # 定义一个字符串变量

print(str)           # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（不包含索引为 5 的字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起
执行以上程序会输出如下结果：

Runoob
Runoo
R
noo
noob
RunoobRunoob
RunoobTEST
Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：

实例
>>> print('Ru\noob')
Ru
oob
>>> print(r'Ru\noob')
Ru\noob
>>>
'''
# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
'''
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

实例
>>> word = 'Python'
>>> print(word[0], word[5])
P n
>>> print(word[-1], word[-6])
n P
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。

注意：

1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''
print('test' + ' python3')
str = 'test'
# str[0] = 'h' # TypeError: 'str' object does not support item assignment
print(str)

'''
bool（布尔类型）
布尔类型即 True 或 False。

在 Python 中，True 和 False 都是关键字，表示布尔值。

布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。

布尔类型特点：

布尔类型只有两个值：True 和 False。

bool 是 int 的子类，因此布尔值可以被看作整数来使用，其中 True 等价于 1。

布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。

布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。

布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。

可以使用 bool() 函数将其他类型的值转换为布尔值。以下值在转换为布尔值时为 False：None、False、零 (0、0.0、0j)、空序列（如 ''、()、[]）和空映射（如 {}）。其他所有值转换为布尔值时均为 True。
'''
# 布尔类型的值和类型
a = True
b = False
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

# 布尔类型的整数表现
print(int(True),int(False)) # 1 0

# 使用 bool()函数进行转换
print(bool(0),bool(''),bool([])) # False
print(bool(42),bool('python'),bool([1,2,3])) # True

# 布尔逻辑运算
print( True and False) # False
print( True or False) # True
print(not True) # False

# 布尔比较运算
print(5 > 3) # True
print(2 == 2) # True
print(7 < 4) # False

# 布尔值在控制流中的应用
if True:
    print("this will always print")
if not False:
    print('this will also always print')

x = 10
if x:
    print('x is non-zero and thus True in a boolean context')

'''
注意: 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
'''

'''
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。



加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：

实例
'''
list = ['abcd',786,2.23,'test',-70.2] # 定义1个列表
tinylist = [123,'test']

print(list) # 打印整个列表
print(list[0]) # 打印列表的第1个元素
print(list[1:3]) # 打印列表第2到第4个元素（不包含第4个元素）
print(list[2:]) # 打印列表从第3个元素开始到末尾
print(tinylist * 2) # 打印tinylist列表2次
print(list + tinylist) # 打印2个列表拼接在一起的结果

# 执行结果
'''
['abcd', 786, 2.23, 'test', -70.2]
abcd
[786, 2.23]
[2.23, 'test', -70.2]
[123, 'test', 123, 'test']
['abcd', 786, 2.23, 'test', -70.2, 123, 'test']
'''
# 与Python字符串不一样的是，列表中的元素是可以改变的：
list2 = [1,2,3,4,5,6]
list2[0] = 9
list2[2:5] = [13,14,15]
print(list2) # [9, 2, 13, 14, 15, 6]
list2[2:5] = [] # 将对应的元素设置为[]
print(list2) # [9, 2, 6]

'''
List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。

注意：

1、列表写在方括号之间，元素用逗号隔开。
2、和字符串一样，列表可以被索引和切片。
3、列表可以使用 + 操作符进行拼接。
4、列表中的元素是可以改变的。
Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
'''
list3 = [0,1,2,3,4,5]
print(list3[1:4:2]) # 1,3

# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input):

    # 通过空搞将字符串分割，把各个单词分割为列表
    inputWords = input.split(' ')

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like python3'
    rw = reverseWords(input)
    print(rw)

'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：
'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

# 执行结果
'''
('abcd', 786, 2.23, 'runoob', 70.2)
abcd
(786, 2.23)
(2.23, 'runoob', 70.2)
(123, 'runoob', 123, 'runoob')
('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')
'''

'''
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
'''
tup = (1,2,3,4,5,6)
print(tup[0]) # 1
print(tup[1:5]) # (2, 3, 4, 5)
# tup[0] = 11 # 修改元组元素的操作是非法的 TypeError: 'tuple' object does not support item assignment

'''
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，Python会将括号解释为数学运算中的括号，而不是元组的表示。

如果不添加逗号，如下所示，它将被解释为一个普通的值而不是元组：

not_a_tuple = (42)
这样的话，not_a_tuple 将是整数类型而不是元组类型。

string、list 和 tuple 都属于 sequence（序列）。

注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用 + 操作符进行拼接。
'''
tup1 = () # 空元组
tup2 = (20,) # 1个元素，必须要在元素后加逗号，否则会认为是数学运算中的括号，从而变成1个整型
not_a_tuple = (20)
print(type(tup1))
print(type(tup2))
print(type(not_a_tuple))

'''
结果：
<class 'tuple'>
<class 'tuple'>
<class 'int'>
'''

'''
Set（集合）
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。

另外，也可以使用 set() 函数创建集合。

注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)
'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Zhihu'}

print(sites) # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runnob 不在集合中')

# set可以进行集合运算
set1 = set('abracadabra')
set2 = set('alacazam')

print(set1)
print(set1 - set2) # 差集
print(set1 | set2) # 并集
print(set1 & set2) # 交集
print(set1 ^ set2) # 2个集合中都不存在的元素

'''
以上实例输出结果：

{'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
Runoob 在集合中
{'b', 'c', 'a', 'r', 'd'}
{'r', 'b', 'd'}
{'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
{'c', 'a'}
{'z', 'b', 'm', 'r', 'l', 'd'}
'''

'''
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
'''
dict1 = {}
dict1['one'] = '1-菜鸟教程'
dict1[2] = '2-菜鸟工具'

tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}

print(dict1['one'])
print(dict1[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

'''
结果：

1-菜鸟教程
2-菜鸟工具
{'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict_keys(['name', 'code', 'site'])
dict_values(['runoob', 1, 'www.runoob.com'])
'''

'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：

实例
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}

{x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式，更多推导式内容可以参考：Python 推导式。

另外，字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。

注意：

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
'''
dict2 = dict([('Runoob',1),('Google',2),('Taobao',3)])
print(dict2)
dict3 = {x:x**2 for x in(2,4,6)}
print(dict3)
dict4 = dict(Runoob=1,Google=2,Taobao=3)
print(dict4)

'''
执行结果：
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
{2: 4, 4: 16, 6: 36}
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
'''


'''
bytes 类型
在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。

与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。

bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。

创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：

此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：

x = bytes("hello", encoding="utf-8")
与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。例如：

实例

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。例如：

实例
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
其中 ord() 函数用于将字符转换为相应的整数值。
'''
b1 = b'hello'
b2 = b1[1:3] # 切片操作，得到 b'el'
b3 = b1 + b'world' # 拼接操作，得到 b'helloworld'

print(b1,b2,b3) # b'hello' b'el' b'helloworld'

if b1[0] == ord('h'):
    print("the first element is h")
