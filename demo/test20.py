#!/usr/bin/python3

'''
Python3 集合
集合（set）是一个无序的不重复元素序列。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

创建格式：

parame = {value01,value02,...}
或者
set(value)
以下是一个简单实例：

set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

更多实例演示：

实例(Python 3.0+)
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 快速判断元素是否在集合内
True
>>> 'crabgrass' in basket
False

>>> # 下面展示两个集合间的运算.
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
类似列表推导式，同样集合支持集合推导式(Set comprehension):

实例(Python 3.0+)
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
集合的基本操作
1、添加元素
语法格式如下：

s.add( x )
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.add("Facebook")
>>> print(thisset)
{'Taobao', 'Facebook', 'Google', 'Runoob'}
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

s.update( x )
x 可以有多个，用逗号分开。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.update({1,3})
>>> print(thisset)
{1, 3, 'Google', 'Taobao', 'Runoob'}
>>> thisset.update([1,4],[5,6])  
>>> print(thisset)
{1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
>>>
2、移除元素
语法格式如下：

s.remove( x )
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.remove("Taobao")
>>> print(thisset)
{'Google', 'Runoob'}
>>> thisset.remove("Facebook")   # 不存在会发生错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Facebook'
>>>
此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

s.discard( x )
实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.discard("Facebook")  # 不存在不会发生错误
>>> print(thisset)
{'Taobao', 'Google', 'Runoob'}
我们也可以设置随机删除集合中的一个元素，语法格式如下：

s.pop() 
脚本模式实例(Python 3.0+)
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()

print(x)
输出结果：

Runoob
多次执行测试结果都不一样。

set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

3、计算集合元素个数
语法格式如下：

len(s)
计算集合 s 元素个数。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> len(thisset)
3
4、清空集合
语法格式如下：

s.clear()
清空集合 s。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.clear()
>>> print(thisset)
set()
5、判断元素是否在集合中存在
语法格式如下：

x in s
判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

实例(Python 3.0+)
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> "Runoob" in thisset
True
>>> "Facebook" in thisset
False
>>>
集合内置方法完整列表
方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
len()	计算集合元素个数
'''
set1 = {1,2,3,4,5,1} # 直接使用大括号创建集合
set2 = set([1,2,3,4,5,1,2]) # 使用set()函数从列表创建集合，创建空集合必须用set(),因为{}是创建1个空字典
set3 = set([])
dict1 = {}
print(set1,set2,set3,dict1)
print(type(set1),type(set2),type(set3),type(dict1))

'''
结果：
{1, 2, 3, 4, 5} {1, 2, 3, 4, 5} set() {}
<class 'set'> <class 'set'> <class 'set'> <class 'dict'>
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # 演示去重功能
print('orange' in basket) # 快速判断元素是否在集合内
print('cc' in basket) # 快速判断元素是否在集合内
# 下面演示2个集合直接的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b) # 集合a中包含，而集合b不包含的元素
print(a|b) # 并集，集合a 或 b 中所有的元素
print(a&b) # 交集，集合a 和 b 都包含的元素
print(a^b) # 不同时包含于a和b的元素

'''
结果：
{'r', 'd', 'a', 'c', 'b'}
{'r', 'b', 'd'}
{'r', 'd', 'a', 'l', 'm', 'z', 'c', 'b'}
{'a', 'c'}
{'r', 'm', 'd', 'l', 'b', 'z'}

'''
# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'d', 'r'}

# 1.添加元素
thisset = set(('Google','Runoob','Taobao'))
# thisset = set(['Google','Runoob','Taobao'])
thisset.add('Facebook')
print(thisset)

# 还有1个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下 s.update(x)
# x 可以有多个，用逗号分开
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])
print(thisset)
thisset.update((7,8,9))
print(thisset)
thisset.update({'name':'rockey'})
print(thisset)

'''
结果：
{'Facebook', 'Runoob', 'Google', 'Taobao'}
{1, 'Facebook', 3, 'Runoob', 'Google', 'Taobao'}
{1, 'Facebook', 3, 4, 5, 6, 'Runoob', 'Google', 'Taobao'}
{1, 'Facebook', 3, 4, 5, 6, 7, 8, 9, 'Runoob', 'Google', 'Taobao'}
{1, 'Facebook', 3, 4, 5, 6, 7, 8, 9, 'Runoob', 'Google', 'name', 'Taobao'}
'''

# 2.移除元素
thisset.remove('Taobao')
print(thisset)
# thisset.remove('test') # KeyError: 'test'

# 还有1个方法，移除集合中的元素，且如果元素不存在，不发送错误。s.discard(x)
thisset.discard('test') # 不存在不发生错误
# 我们也可以随机删除其中1个元素。 s.pop()
thisset = set(("Google",'Runoob'))
x = thisset.pop()
print(x)
print(thisset.pop())
# thisset.pop() # KeyError: 'pop from an empty set'

# 3.计算集合元素个数
thisset = set(("Google", "Runoob", "Taobao"))
print(len(thisset))

# 4.清空集合
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset) # set() 空集合

# 5.判断元素是否在集合中存在 语法格式如下：x in s
thisset = set(("Google", "Runoob", "Taobao"))
print('Runoob' in thisset) # True
print('Facebook' in thisset) # False

'''
copy() 方法用于拷贝一个集合。

语法
copy() 方法语法：

set.copy()
参数
无。
返回值
返回拷贝的集合。

实例
拷贝 fruits 集合：

实例 1
sites = {"Google", "Runoob", "Taobao"}
x = sites.copy()
print(x)
输出结果为：

set(['Google', 'Taobao', 'Runoob'])
'''
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset.copy())

'''
difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。

语法
difference() 方法语法：

set.difference(set)
参数
set -- 必需，用于计算差集的集合
返回值
返回一个新的集合。

实例
返回一个集合，元素包含在集合 x ，但不在集合 y ：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
z = x.difference(y) 
 
print(z)
输出结果为：

{'cherry', 'banana'}
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.difference(y)) # 差集 {"banana", "cherry"}
print(x-y) # 差集 {"banana", "cherry"}

'''
difference_update() 方法用于移除两个集合中都存在的元素。

difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。

语法
difference_update() 方法语法：

set.difference_update(set)
参数
set -- 必需，用于计算差集的集合
返回值
无。

实例
移除两个集合都包含的元素：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
x.difference_update(y) 
 
print(x)
输出结果为：

{'cherry', 'banana'}
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.difference_update(y)) # 无返回值
print(x) # {'cherry', 'banana'}

'''
intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。

语法
intersection() 方法语法：

set.intersection(set1, set2 ... etc)
参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
返回值
返回一个新的集合。

实例
返回一个新集合，该集合的元素既包含在集合 x 又包含在集合 y 中：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
z = x.intersection(y) 
 
print(z)
输出结果为：

{'apple'}
计算多个集合的交集：

实例 1
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
 
result = x.intersection(y, z)
 
print(result)
输出结果为：

{'c'}
'''
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
print(x.intersection(y)) # 交集 {'apple'}
print(x&y) # 交集 {'apple'}

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
print(x.intersection(y,z)) # 交集 {'c'}
print(x&y&z)  # 交集 {'c'}

'''
intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。

intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。

语法
intersection_update() 方法语法：

set.intersection_update(set1, set2 ... etc)
参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
返回值
无。

实例
移除 x 集合中不存在于 y 集合中的元素：

实例 1
x = {"apple", "banana", "cherry"}  # y 集合不包含 banana 和 cherry，被移除 
y = {"google", "runoob", "apple"}
 
x.intersection_update(y) 
 
print(x)
输出结果为：

{'apple'}
计算多个集合的交集：

实例 1
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
 
x.intersection_update(y, z)
 
print(x)
输出结果为：

{'c'}
'''
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

print(x.intersection_update(y,z)) # None 无返回值
print(x) # 交集 {'c'}

'''
isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。

语法
isdisjoint() 方法语法：

set.isdisjoint(set)
参数
set -- 必需，要比较的集合
返回值
返回布尔值，如果不包含返回 True，否则返回 False。

实例
判断集合 y 中是否有包含 集合 x 的元素：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
 
z = x.isdisjoint(y) 
 
print(z)
输出结果为：

True
如果包含返回 False：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
z = x.isdisjoint(y) 
 
print(z)
输出结果为：

False
'''
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
print(x.isdisjoint(y)) # True 没有相同的元素，返回True

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
print(x.isdisjoint(y)) # False 有相同的元素

'''
issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。

语法
issubset() 方法语法：

set.issubset(set)
参数
set -- 必需，要比查找的集合
返回值
返回布尔值，如果都包含返回 True，否则返回 False。

实例
判断集合 x 的所有元素是否都包含在集合 y 中：

实例 1
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
 
z = x.issubset(y) 
 
print(z)
输出结果为：

True
如果没有全部包含返回 False：

实例 1
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
 
z = x.issubset(y) 
 
print(z)
输出结果为：

False
'''
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y)) # x 是 y 的子集，返回 True

x = {"a", "b", "c",'g'}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y)) # x 不是 y 的子集，返回 False

'''
issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。

语法
issuperset() 方法语法：

set.issuperset(set)
参数
set -- 必需，要比查找的集合
返回值
返回布尔值，如果都包含返回 True，否则返回 False。

实例
判断集合 y 的所有元素是否都包含在集合 x 中：

实例 1
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
 
z = x.issuperset(y) 
 
print(z)
输出结果为：

True
如果没有全部包含返回 False：

实例 1
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
 
z = x.issuperset(y) 
 
print(z)
输出结果为：

False
'''
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"} 
print(x.issuperset(y)) # y 是 x 的子集，返回 True

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c",'g'} 
print(x.issuperset(y)) # y 不是 x 的子集，返回 False

# ps注意 issubset 和 issuperset 是相反的


'''
symmetric_difference() 方法可以用来找到两个集合的对称差。

symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。

语法
symmetric_difference() 方法语法：

set.symmetric_difference(set)
参数
set -- 集合
返回值
返回一个新的集合。

实例
返回两个集合组成的新集合，但会移除两个集合的重复元素：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
z = x.symmetric_difference(y) 
 
print(z)
输出结果为：

{'google', 'cherry', 'banana', 'runoob'}
你还可以使用 ^ 运算符来实现相同的效果：

实例
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1 ^ set2
print(result)  # 输出: {1, 2, 5, 6}
输出结果为：

{1, 2, 5, 6}
'''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 ^ set2) # {1, 2, 5, 6} 取2个集合的交集之外的所有元素。
print(set1.symmetric_difference(set2)) #  {1, 2, 5, 6} 取2个集合的交集之外的所有元素。

'''
symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。

语法
symmetric_difference_update() 方法语法：

set.symmetric_difference_update(set)
参数
set -- 要检测的集合
返回值
无。

实例
在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的元素插入到集合 x 中：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
x.symmetric_difference_update(y) 
 
print(x)
输出结果为：

{'google', 'cherry', 'banana', 'runoob'}
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.symmetric_difference_update(set2)) # None 无返回值
print(set1) #  {1, 2, 5, 6} 取2个集合的交集之外的所有元素。


'''
union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。

语法
union() 方法语法：

set.union(set1, set2...)
参数
set1 -- 必需，合并的目标集合
set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
返回值
返回一个新集合。

实例
合并两个集合，重复元素只会出现一次：

实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
z = x.union(y) 
 
print(z)
输出结果为：

{'cherry', 'runoob', 'google', 'banana', 'apple'}
合并多个集合：

实例 1
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
 
result = x.union(y, z) 
 
print(result)
输出结果为：

{'c', 'd', 'f', 'e', 'b', 'a'}
'''
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
print(x|y|z) # 并集 {'c', 'f', 'b', 'e', 'a', 'd'}
print(x.union(y,z)) # 并集 {'c', 'f', 'b', 'e', 'a', 'd'}