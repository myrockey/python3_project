#!/usr/bin/python3

'''
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2, key3 : value3 }
注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。



键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

一个简单的字典实例：

tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}


也可如此创建字典：

tinydict1 = { 'abc': 456 }
tinydict2 = { 'abc': 123, 98.6: 37 }
创建空字典
使用大括号 { } 创建空字典：

实例
# 使用大括号 {} 来创建空字典
emptyDict = {}
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:", len(emptyDict))
 
# 查看类型
print(type(emptyDict))
以上实例输出结果：

{}
Length: 0
<class 'dict'>
使用内建函数 dict() 创建字典：

实例
emptyDict = dict()
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:",len(emptyDict))
 
# 查看类型
print(type(emptyDict))
以上实例输出结果：

{}
Length: 0
<class 'dict'>
访问字典里的值
把相应的键放入到方括号中，如下实例:

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])
以上实例输出结果：

tinydict['Name']:  Runoob
tinydict['Age']:  7
如果用字典里没有的键访问数据，会输出错误如下：

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Alice']: ", tinydict['Alice'])
以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print ("tinydict['Alice']: ", tinydict['Alice'])
KeyError: 'Alice'

修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])
以上实例输出结果：
tinydict['Age']:  8
tinydict['School']:  菜鸟教程

删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。

显式删除一个字典用del命令，如下实例：

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])
但这会引发一个异常，因为用执行 del 操作后字典不再存在：

Traceback (most recent call last):
  File "/runoob-test/test.py", line 9, in <module>
    print ("tinydict['Age']: ", tinydict['Age'])
NameError: name 'tinydict' is not defined
注：del() 方法后面也会讨论。


字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：


1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：


实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
 
print ("tinydict['Name']: ", tinydict['Name'])
以上实例输出结果：

tinydict['Name']:  小菜鸟
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

实例
#!/usr/bin/python3
 
tinydict = {['Name']: 'Runoob', 'Age': 7}
 
print ("tinydict['Name']: ", tinydict['Name'])
以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 3, in <module>
    tinydict = {['Name']: 'Runoob', 'Age': 7}
TypeError: unhashable type: 'list'

字典内置函数&方法
Python字典包含了以下内置函数：

序号	函数及描述	实例
1	len(dict)
计算字典元素个数，即键的总数。	
>>> tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(tinydict)
3
2	str(dict)
输出字典，可以打印的字符串表示。	
>>> tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(tinydict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(tinydict)
<class 'dict'>
Python字典包含了以下内置方法：

序号	函数及描述
1	dict.clear()
删除字典内所有元素
2	dict.copy()
返回一个字典的浅复制
3	dict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	dict.get(key, default=None)
返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	dict.items()
以列表返回一个视图对象
7	dict.keys()
返回一个视图对象
8	dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)
把字典dict2的键/值对更新到dict里
10	dict.values()
返回一个视图对象
11	dict.pop(key[,default])
删除字典 key（键）所对应的值，返回被删除的值。
12	dict.popitem()
返回并删除字典中的最后一对键和值。
'''
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(tinydict)
print(str(tinydict))

'''
结果：
{'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
{'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
'''

tinydict = {'Name': 'Zara', 'Age': 7}

print ("字典长度 : %d" %  len(tinydict))
tinydict.clear()
print ("字典删除后长度 : %d" %  len(tinydict))

'''
以上实例输出结果为：

字典长度 : 2
字典删除后长度 : 0
'''

'''
描述
Python 字典 copy() 函数返回一个字典的浅复制。

语法
copy()方法语法：

dict.copy()
参数
NA。
返回值
返回一个字典的浅复制。

实例
以下实例展示了 copy()函数的使用方法：

实例
#!/usr/bin/python3
 
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)
以上实例输出结果为：

新复制的字典为 :  {'Age': 7, 'Name': 'Runoob', 'Class': 'First'}
直接赋值和 copy 的区别
可以通过以下实例说明：

实例
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1)
print(dict2)
print(dict3)
实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。

{'user': 'root', 'num': [2, 3]}
{'user': 'root', 'num': [2, 3]}
{'user': 'runoob', 'num': [2, 3]}
'''

'''
Python 直接赋值、浅拷贝和深度拷贝解析
分类 编程技术
直接赋值：其实就是对象的引用（别名）。

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

字典浅拷贝实例
实例
>>>a = {1: [1,2,3]}
>>> b = a.copy()
>>> a, b
({1: [1, 2, 3]}, {1: [1, 2, 3]})
>>> a[1].append(4)
>>> a, b
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
深度拷贝需要引入 copy 模块：

实例
>>>import copy
>>> c = copy.deepcopy(a)
>>> a, c
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
>>> a[1].append(5)
>>> a, c
({1: [1, 2, 3, 4, 5]}, {1: [1, 2, 3, 4]})
解析
1、b = a: 赋值引用，a 和 b 都指向同一个对象。



2、b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。



b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。



更多实例
以下实例是使用 copy 模块的 copy.copy（ 浅拷贝 ）和（copy.deepcopy ）:

实例
#!/usr/bin/python
# -*-coding:utf-8 -*-
 
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )
以上实例执行输出结果为：

('a = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('b = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('c = ', [1, 2, 3, 4, ['a', 'b', 'c']])
('d = ', [1, 2, 3, 4, ['a', 'b']])
'''
import copy
a = [1,2,3,4,['a','b']] # 原始对象

b = a # 赋值，传对象的引用
c = copy.copy(a) # 对象拷贝，浅拷贝
d = copy.deepcopy(a) # 对象拷贝，深拷贝

a.append(5) # 修改对象a
a[4].append('c') # 修改对象a中的['a','b']列表对象

print( 'a = ',a)
print( 'b = ',b)
print( 'c = ',c)
print( 'd = ',d)

'''
结果：
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
'''

'''
描述
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

语法
fromkeys() 方法语法：

dict.fromkeys(seq[, value])
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
返回值
该方法返回一个新字典。

实例
以下实例展示了 fromkeys()函数的使用方法：

实例
#!/usr/bin/python3
 
seq = ('name', 'age', 'sex')
 
tinydict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(tinydict))
 
tinydict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(tinydict))
以上实例输出结果为：

新的字典为 : {'age': None, 'name': None, 'sex': None}
新的字典为 : {'age': 10, 'name': 10, 'sex': 10}
不指定值：

实例
#!/usr/bin/python3
 
x = ('key1', 'key2', 'key3')
 
thisdict = dict.fromkeys(x)
 
print(thisdict)
以上实例输出结果为：

{'key1': None, 'key2': None, 'key3': None}
'''

seq = ('name','age','sex')

dict1 = dict.fromkeys(seq)
print("新的字典：%s" % str(dict1))

dict1 = dict.fromkeys(seq,10)
print("新的字典：%s" % str(dict1))

'''
结果：
新的字典：{'name': None, 'age': None, 'sex': None}
新的字典：{'name': 10, 'age': 10, 'sex': 10}
'''

'''
描述
Python 字典 get() 函数返回指定键的值。

语法
get()方法语法：

dict.get(key[, value]) 
参数
key -- 字典中要查找的键。
value -- 可选，如果指定键的值不存在时，返回该默认值。
返回值
返回指定键的值，如果键不在字典中返回默认值，如果不指定默认值，则返回 None。

实例
以下实例展示了 get() 函数的使用方法：

实例
#!/usr/bin/python

tinydict = {'Name': 'Runoob', 'Age': 27}

print ("Age : ", tinydict.get('Age'))

# 没有设置 Sex，也没有设置默认的值，输出 None
print ("Sex : ", tinydict.get('Sex'))  

# 没有设置 Salary，输出默认的值  0.0
print ('Salary: ', tinydict.get('Salary', 0.0))
以上实例输出结果为：

Age : 27
Sex : None
Salary: 0.0
get() 方法 Vs dict[key] 访问元素区别
get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。

dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。

实例
>>> runoob = {}
>>> print('URL: ', runoob.get('url'))     # 返回 None
URL:  None

>>> print(runoob['url'])     # 触发 KeyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'url'
>>>
嵌套字典使用
get() 方法对嵌套字典的使用方法如下：

实例
#!/usr/bin/python

tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'}}

res = tinydict.get('RUNOOB', {}).get('url')
# 输出结果
print("RUNOOB url 为 : ", str(res))
以上实例输出结果为：

RUNOOB url 为 :  www.runoob.com
'''
tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'}}

res = tinydict.get('RUNOOB', {}).get('url')
# 输出结果
print("RUNOOB url 为 : ", str(res)) # 没找到对应的键 不会报错 ，返回默认值 None 
print(tinydict['RUNOOB']['url']) # 没找到对应的键 会报错

'''
Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。

而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。

语法
in 操作符语法：

key in dict
参数
key -- 要在字典中查找的键。
返回值
如果键在字典里返回true，否则返回false。

实例
以下实例展示了 in 操作符在字典中的使用方法：

实例(Python 3.0+)
#!/usr/bin/python3
 
thisdict = {'Name': 'Runoob', 'Age': 7}
 
# 检测键 Age 是否存在
if  'Age' in thisdict:
    print("键 Age 存在")
else :
    print("键 Age 不存在")
 
# 检测键 Sex 是否存在
if  'Sex' in thisdict:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")
 
 
# not in
 
# 检测键 Age 是否不存在
if  'Age' not in thisdict:
    print("键 Age 不存在")
else :
    print("键 Age 存在")
以上实例输出结果为：

键 Age 存在
键 Sex 不存在
键 Age 存在
'''


'''
描述
Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。

dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。

视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。

我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。

语法
items()方法语法：

dict.items()
参数
NA。
返回值
返回可视图对象。

实例
以下实例展示了 items() 方法的使用方法：

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Value : %s" %  tinydict.items())
以上实例输出结果为：

Value : dict_items([('Age', 7), ('Name', 'Runoob')])
'''
 
tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Value : %s" %  tinydict.items())

'''
描述
Python3 字典 keys() 方法返回一个视图对象。

dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。

视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。

我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。

注意：Python2.x 是直接返回列表

语法
keys()方法语法：

dict.keys()
参数
NA。
返回值
返回一个视图对象。

实例
以下实例展示了 keys() 方法的使用方法：

实例
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()

>>> # 迭代
>>> n = 0
>>> for val in values:
...     n += val
>>> print(n)
504

>>> # keys 和 values 以相同顺序（插入顺序）进行迭代
>>> list(keys)     # 使用 list() 转换为列表
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # 视图对象是动态的，受字典变化的影响，以下删除了字典的 key，视图对象转为列表后也跟着变化
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']
'''
dishes = {'eggs':2,'sausage':1,'bacon':1,'spam':500}
keys = dishes.keys()
values = dishes.values()
# 迭代
n = 0
for val in values:
    n += val
print(n)

# keys values 以相同顺序(插入顺序)进行迭代
print(list(keys),list(values))

# 视图对象是动态的，受字典变化的影响，以下删除了字典的key，视图对象转为列表后也跟着变化
del dishes['eggs']
del dishes['sausage']
print(list(keys))

'''
Python 字典 setdefault() 方法和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

语法
setdefault()方法语法：

dict.setdefault(key, default=None)
参数
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
返回值
如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。

实例
以下实例展示了 setdefault() 方法的使用方法：

实例
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Age 键的值为 : %s" %  tinydict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  tinydict.setdefault('Sex', None))
print ("新字典为：", tinydict)
以上实例输出结果为：

Age 键的值为 : 7
Sex 键的值为 : None
新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
'''
tinydict2 = {'name':'rockey','age':18}
print("age=%s " % tinydict2.setdefault('age',None))
print("sex=%s" % tinydict2.setdefault('sex',None))

'''
Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。

语法
update() 方法语法：

dict.update(dict2)
参数
dict2 -- 添加到指定字典dict里的字典。
返回值
该方法没有任何返回值。

实例
以下实例展示了 update()函数的使用方法：

实例(Python 2.0+)
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Sex': 'female' }
 
tinydict.update(tinydict2)
print ("更新字典 tinydict : ", tinydict)

以上实例输出结果为：

更新字典 tinydict :  {'Name': 'Runoob', 'Age': 7, 'Sex': 'female'}
'''
tdict = {'name':'rockey','age':18}
tdict2 = {'sex':'female'}

tdict.update(tdict2)
print("更新字典 tdict : ",tdict)

tdict2 = {'age':22}
tdict.update(tdict2)
print("更新字典 tdict : ",tdict)

#相同两个 dict.values() 比较返回都是 False
d = {'a': 1}
v1 = d.values()
v2 = d.values()
print(v1 == v2) # False
print(v1 is v2) # False
print(list(v1) == list(v2)) # True

'''
原因不是“值不相等”，而是 dict.values() 返回的是一个 视图对象（dict_values 类型），
Python 的 == 对这种内置视图类型根本没有定义（回退到 is），
所以两次调用生成的两个不同对象在身份比较时永远为 False。
验证：
Python
复制
d = {'a': 1}
v1 = d.values()
v2 = d.values()
print(v1 == v2)   # False
print(v1 is v2)   # False
print(list(v1) == list(v2))  # True，把视图转成列表再比就相等
因此
Python
复制
print(d.values() == d.values())
必然输出 False，这是由“视图对象不可比”而非“值不同”导致的。
'''


'''
描述
Python 字典 pop() 方法删除字典 key（键）所对应的值，返回被删除的值。如果键不存在，则可以选择返回一个默认值（如果提供了）。

语法
pop()方法语法：

dict.pop(key, default)
参数
key：要移除的键。
default（可选）：如果键不存在时，返回的默认值。如果没有提供默认值且键不存在，会引发 KeyError 异常。
返回值
返回被删除的值：

如果 key 存在 - 删除字典中对应的元素
如果 key 不存在 - 返回设置指定的默认值 default
如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
实例
以下实例展示了 pop() 方法的使用方法：

实例
#!/usr/bin/python3

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

element = site.pop('name')

print('删除的元素为:', element)
print('字典为:', site)
输出结果为：

删除的元素为: 菜鸟教程
字典为: {'alexa': 10000, 'url': 'www.runoob.com'}
如果删除的键不存在会触发异常：

实例
#!/usr/bin/python3

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

element = site.pop('nickname')

print('删除的元素为:', element)
print('字典为:', site)
输出结果为：

File "/Users/RUNOOB/runoob-test/test.py", line 5, in <module>
    element = site.pop('nickname')
KeyError: 'nickname'
可以设置默认值来避免异常：

实例
#!/usr/bin/python3

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

element = site.pop('nickname', '不存在的 key')

print('删除的元素为:', element)
print('字典为:', site)
输出结果为：

 
删除的元素为: 不存在的 key
字典为: {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
'''
site = {'name':'菜鸟教程','alexa':10000,'url':'www.runoob.com'}
element = site.pop('name')
print('del element:',element)
print('site:',site)

# 不存在的key删除会触发异常
# element = site.pop('nickname') # KeyError: 'nickname'
# print('del element:',element)

# 设置默认值来避免异常
element = site.pop('nickname','不存在的 key')
print('del element:',element)

'''
Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法
popitem()方法语法：

popitem()
参数
无
返回值
返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。

注意：在 Python3.7 之前，popitem() 方法删除并返回任意插入字典的键值对。

实例
以下实例展示了 popitem() 方法的使用方法：

实例
#!/usr/bin/python3

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)

# 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)

# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)
输出结果为：

返回值 =  ('url', 'www.runoob.com')
site =  {'name': '菜鸟教程', 'alexa': 10000}
site =  {'name': '菜鸟教程', 'alexa': 10000, 'nickname': 'Runoob'}
返回值 =  ('nickname', 'Runoob')
site =  {'name': '菜鸟教程', 'alexa': 10000}
'''
res = site.popitem()
print(res) # ('url', 'www.runoob.com')

res = site.popitem()
print(res) # ('alexa', 10000)

# res = site.popitem() # KeyError: 'popitem(): dictionary is empty'
# print(res) 