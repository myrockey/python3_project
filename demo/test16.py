#!/usr/bin/python3

'''
Python3 center()方法
Python3 字符串 Python3 字符串

center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

语法
center()方法语法：

str.center(width[, fillchar])
参数
width -- 字符串的总宽度。
fillchar -- 填充字符。
返回值
返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。

实例
以下实例展示了center()方法的实例：
'''
str = '测试居中'
print(str.center(50,'*'))

'''
描述
count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

语法
count()方法语法：

str.count(sub, start= 0,end=len(string))
参数
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
返回值
该方法返回子字符串在字符串中出现的次数。

实例
以下实例展示了 count() 方法的实例：
'''
str2 = 'www.runoob.com'
sub = 'o'
print('str.count(\'o\'):',str2.count(sub))

sub = 'run'
print('str.count(\'run\'):',str2.count(sub))

'''
执行结果：

str.count('o'): 3
str.count('run'): 1
'''

'''
描述
decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。

语法
decode()方法语法：

bytes.decode(encoding="utf-8", errors="strict")
参数
encoding -- 要使用的编码，如"UTF-8"。
errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
返回值
该方法返回解码后的字符串。

实例
以下实例展示了decode()方法的实例：
'''
str3 = '菜鸟教程'
str_utf8 = str3.encode('UTF-8')
str_gbk = str3.encode("GBK")

print(str3)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

'''
描述
endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。

语法
endswith()方法语法：

str.endswith(suffix[, start[, end]])
参数
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。
返回值
如果字符串含有指定的后缀返回 True，否则返回 False。

实例
以下实例展示了endswith()方法的实例：
'''
str5 = 'Runoob example....wow!!!'
suffix = '!!'
print(str5.endswith(suffix))
print(str5.endswith(suffix,20))
suffix = 'run'
print(str5.endswith(suffix))
print(str5.endswith(suffix,0,19))

'''
以上实例输出结果如下：

True
True
False
False
'''

'''
描述
expandtabs() 方法把字符串中的 tab 符号 \t 转为空格，tab 符号 \t 默认的空格数是 8，在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。

语法
expandtabs() 方法语法：

str.expandtabs(tabsize=8)
参数
tabsize -- 指定转换字符串中的 tab 符号 \t 转为空格的字符数。
返回值
该方法返回字符串中的 tab 符号 \t 转为空格后生成的新字符串。

实例
以下实例展示了 expandtabs() 方法的实例：
'''
str6 = "runoob\t12345\tabc"  
print('原始字符串:', str6)
 
# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号:', str6.expandtabs())
 
# 2 个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号:', str6.expandtabs(2))
 
# 3 个空格
print('使用 3 个空格:', str6.expandtabs(3))
 
# 4 个空格
print('使用 4 个空格:', str6.expandtabs(4))
 
# 5 个空格
print('使用 5 个空格:', str6.expandtabs(5))
 
# 6 个空格
print('使用 6 个空格:', str6.expandtabs(6))

'''
以上实例输出结果如下：

原始字符串: runoob      12345   abc
替换 \t 符号: runoob  12345   abc
使用 2 个空格替换 \t 符号: runoob  12345 abc
使用 3 个空格: runoob   12345 abc
使用 4 个空格: runoob  12345   abc
使用 5 个空格: runoob    12345     abc
使用 6 个空格: runoob      12345 abc
'''


'''
find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

语法
find()方法语法：

str.find(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
返回值
如果包含子字符串返回开始的索引值，否则返回-1。

实例
以下实例展示了find()方法的实例：
'''
 
str7 = "Runoob example....wow!!!"
str8 = "exam"
 
print (str7.find(str8))
print (str7.find(str8, 5))
print (str7.find(str8, 10))


'''
isalnum() 方法用于检查字符串是否由字母和数字组成，即字符串中的所有字符都是字母或数字。

空字符串：如果字符串为空（长度为0），则返回 False，因为空字符串不包含任何字母或数字。
大小写敏感：isalnum() 方法区分大小写，即只有字母和数字的字符才会被认为是有效的。
特殊字符：特殊字符（如标点符号、空格、特殊符号等）不被认为是字母或数字。
语法
isalnum()方法语法：

str.isalnum()
参数
无。
返回值
如果字符串至少有一个字符，并且所有字符都是字母或数字，则返回 True；否则返回 False。

实例
以下实例展示了isalnum()方法的实例：
'''
str9 = 'runoob2016'
print(str9.isalnum())

str10 = 'www.runoob.com'
print(str10.isalnum()) # 包含符号.

'''
以上实例输出结果如下：

True
False
'''

# 示例 1: 包含字母和数字的字符串
print("abc123".isalnum())  # 输出: True

# 示例 2: 包含空格的字符串
print("abc 123".isalnum())  # 输出: False

# 示例 3: 包含特殊字符的字符串
print("abc#123".isalnum())  # 输出: False

# 示例 4: 空字符串
print("".isalnum())  # 输出: False

# 示例 5: 只包含数字的字符串
print("123456".isalnum())  # 输出: True

# 示例 6: 只包含字母的字符串
print("abcdef".isalnum())  # 输出: True

# 示例 7: 包含下划线但不是字母或数字的字符串
print("abc_def".isalnum())  # 输出: False

'''
Python isalpha() 方法检测字符串是否只由字母或文字组成。

空字符串：如果字符串为空（长度为0），则返回 False，因为空字符串不包含任何字母。
大小写敏感：isalpha() 方法区分大小写，即只有字母的字符才会被认为是有效的。
特殊字符：特殊字符（如标点符号、空格、数字、特殊符号等）不被认为是字母。
语法
isalpha()方法语法：

str.isalpha()
参数
无。
返回值
如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。

实例
以下实例展示了isalpha()方法的实例：
'''
str11 = 'runoob'
print(str11.isalpha())

# 字母和中文文字
str12 = 'runoob菜鸟教程'
print(str12.isalpha())

str13 = 'runoob... test'
print(str13.isalpha())

'''
以上实例输出结果如下：

True
True
False
'''

# 示例 1: 只包含字母的字符串
print("HelloWorld".isalpha())  # 输出: True

# 示例 2: 包含数字的字符串
print("Hello123".isalpha())  # 输出: False

# 示例 3: 包含空格的字符串
print("Hello World".isalpha())  # 输出: False

# 示例 4: 包含特殊字符的字符串
print("Hello#World".isalpha())  # 输出: False

# 示例 5: 空字符串
print("".isalpha())  # 输出: False

# 示例 6: 包含下划线的字符串
print("Hello_World".isalpha())  # 输出: False

# 示例 7: 包含非ASCII字母的字符串
print("HélloWorld".isalpha())  # 输出: True，因为é是字母

'''
描述
Python isdigit() 方法检测字符串是否只由数字组成。

语法
isdigit()方法语法：

str.isdigit()
参数
无。
返回值
如果字符串只包含数字则返回 True 否则返回 False。

实例
以下实例展示了isdigit()方法的实例：

实例
#!/usr/bin/python3

str = "123456";
print (str.isdigit())

str = "Runoob example....wow!!!"
print (str.isdigit())
以上实例输出结果如下：

True
False
isdigit() 方法只对正整数有效，负数及小数均返回不正确。

可以使用以下函数来解决：
'''
print("12345".isdigit()) # True
print("-12345".isdigit()) # False
print("12.3".isdigit()) # False

# 判断是否为数字
def is_number(s):
    try: # 如果能运行 float(s)，返回 True(字符串 s 是浮点数)
        float(s)
        return True
    except ValueError: # ValueError 为 python 的一种标准异常，表示传入无效的参数
        pass # 如果引发了 ValueError 这种异常，不做任何事情（pass不做任何事情，一般用做占位语句）
    try:
        import unicodedata # 处理 ASCII码的包
        unicodedata.numeric(s) # 把1个表示数字的字符串转换位浮点数返回的函数
        return True
    except(TypeError,ValueError):
        pass
        return False

print(is_number(1))
print(is_number(1.0))
print(is_number(0))
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abc"))

'''
输出结果为：

True
True
True
True
True
False
'''

'''
描述
isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。

指数类似 ² 与分数类似 ½ 也属于数字。

# s = '½'
s = '\u00BD'
语法
isnumeric()方法语法：

str.isnumeric()
参数
无。
返回值
如果字符串中只包含数字字符，则返回 True，否则返回 False

实例
以下实例展示了 isnumeric() 方法的实例：

实例
#!/usr/bin/python3

str = "runoob2016"  
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())
以上实例输出结果如下：

False
True
Unicode 数字：

实例
#!/usr/bin/python3

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# s = '½'
s = '\u00BD'
print(s.isnumeric())

a = "\u0030" #unicode for 0
print(a.isnumeric())

b = "\u00B2" #unicode for ²
print(b.isnumeric())

c = "10km2"
print(c.isnumeric())
以上实例输出结果如下：

True
True
True
True
False
'''

'''
描述
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法
join()方法语法：

str.join(sequence)
参数
sequence -- 要连接的元素序列。
返回值
返回通过指定字符连接序列中元素后生成的新字符串。

实例
以下实例展示了join()的使用方法：

实例
#!/usr/bin/python3

s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))

以上实例输出结果如下：

r-u-n-o-o-b
runoob
'''

'''
描述
Python len() 是 Python 内置函数，用于返回对象的长度或元素个数，适用于字符串、列表、元组等具有长度信息的数据类型。

len() 也适用于其他可迭代对象，如集合等。

语法
len()方法语法：

len( s )
参数
s -- 对象。
返回值
返回对象长度。

实例
以下实例展示了 len() 的使用方法：

字符串的长度：

实例
text = "Hello, World!"
length = len(text)
print(length)  # 输出：13
以上实例中，len(text) 返回字符串 text 的字符数，包括空格和标点符号，输出结果为:

13
列表的长度：

实例
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # 输出：5
以上实例中，len(my_list) 返回列表 my_list 中的元素数量，输出结果为:

5
元组的长度：

实例
my_tuple = (10, 20, 30)
length = len(my_tuple)
print(length)  # 输出：3
以上实例中，len(my_tuple) 返回元组 my_tuple 中的元素数量，输出结果为:

3
集合的长度：

实例
my_set = {5, 10, 15, 20}
length = len(my_set)
print(length)  # 输出：4
以上实例中，len(my_set) 返回集合 my_set 中的唯一元素数量，输出结果为:

4
字典的长度：

实例
my_dict = {"apple": 3, "banana": 2, "cherry": 4}
length = len(my_dict)
print(length)  # 输出：3
以上实例中，len(my_dict) 返回字典 my_dict 中键-值对的数量，输出结果为:

3
总之，len() 函数是一个非常实用的工具，用于确定各种类型的序列的长度，这对于编写各种 Python 程序非常有用。

注意事项

对于字符串，len() 返回字符的个数。
对于列表、元组，len() 返回元素的个数。
对于字典，len() 返回键值对的个数。
对于集合，len() 返回集合元素的个数。
'''

'''
描述
ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

语法
ljust()方法语法：

str.ljust(width[, fillchar])
参数
width -- 指定字符串长度。
fillchar -- 填充字符，默认为空格。
返回值
返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

实例
以下实例展示了ljust()的使用方法：

#!/usr/bin/python3

str = "Runoob example....wow!!!"

print (str.ljust(50, '*'))
以上实例输出结果如下：

Runoob example....wow!!!**************************
'''
str15 = 'test ljust'
print(str15.ljust(50,'*'))

'''
描述
lstrip() 方法用于截掉字符串左边的空格或指定字符。

语法
lstrip()方法语法：

str.lstrip([chars])
参数
chars（可选）：指定要移除的字符集合（字符串形式）。

如果省略或为 None，默认移除空白字符（空格、\t、\n、\r、\v、\f）。

注意：chars 是字符集合，不是完整前缀。方法会从左侧开始移除所有在 chars 中出现的字符，直到遇到不在集合中的字符为止。

返回值
返回一个新字符串（原字符串不会被修改）。

关键特性
仅作用于左侧：不影响字符串右侧或中间的字符。

字符集合匹配：chars 是字符集合，不是完整前缀。例如：

"abc123".lstrip("ab")  # 移除 'a' 和 'b' → "c123"
空白字符范围：包括空格、制表符（\t）、换行符（\n）等。

对比其他方法
方法	作用方向	示例
lstrip()	移除左侧字符	" hi ".lstrip() → "hi "
rstrip()	移除右侧字符	" hi ".rstrip() → " hi"
strip()	移除两侧字符	" hi ".strip() → "hi"
'''
text = '  hello,world!   '
print(text.lstrip()) # 输出: "Hello, World!   "（右侧空格保留）

text = "www.example.com"
result = text.lstrip("wcmo.")  # 移除左侧出现的任意字符：w, c, m, o, .
print(result)  # 输出: "example.com"（左侧的 "www." 被移除）

text = "123abc"
result = text.lstrip("321")  # 移除左侧的 '1', '2', '3'（顺序不影响）
print(result)  # 输出: "abc"

text = "123abc"
result = text.lstrip("12")  # 只移除左侧的 '1' 和 '2'，遇到 '3' 停止
print(result)  # 输出: "3abc"

text = "   Hello"
result = text.lstrip()
print(text)   # 输出: "   Hello"（原字符串未修改）
print(result) # 输出: "Hello"

'''
描述
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

两个字符串的长度必须相同，为一一对应的关系。

注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。

语法
maketrans()方法语法：

string.maketrans(x[, y[, z]])
参数
x -- 必需，字符串中要替代的字符组成的字符串。
y -- 可选，相应的映射字符的字符串。
z -- 可选，要删除的字符。
返回值
返回字符串转换后生成的新字符串。

实例
以下实例展示了使用 maketrans() 方法将所有元音字母转换为指定的数字：

实例
'''
# 字母 R 替换为 N
txt = "Runoob!"
mytable = txt.maketrans("R", "N")
print(txt.translate(mytable))

# 使用字符串设置要替换的字符，一一对应
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))
'''
以上实例输出结果如下：

Nunoob!
th3s 3s str3ng 2x1mpl2....w4w!!!
'''


txt = "Google Runoob Taobao!"
x = "mSa"
y = "eJo"
z = "odnght"   # 设置删除的字符
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

'''
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

语法
replace()方法语法：

str.replace(old, new[, max])
参数
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
返回值
返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。

实例
以下实例展示了replace()函数的使用方法：

实例
#!/usr/bin/python3
 
str = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
 
str = "this is string example....wow!!!"
print (str.replace("is", "was", 3))
以上实例输出结果如下：

菜鸟教程旧地址： www.w3cschool.cc
菜鸟教程新地址： www.runoob.com
thwas was string example....wow!!!
'''

'''
Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

语法
splitlines()方法语法：

str.splitlines([keepends])
参数
keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
返回值
返回一个包含各行作为元素的列表。

实例
以下实例展示了splitlines()函数的使用方法：

>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
>>> 
'''

'''
描述
Python title() 方法返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写(见 istitle())。

语法
title()方法语法：

str.title();
参数
NA。
返回值
返回"标题化"的字符串,就是说所有单词的首字母都转化为大写。

实例
以下实例展示了 title()函数的使用方法：

实例(Python 3.0+)
#!/usr/bin/python3
 
str = "this is string example from runoob....wow!!!"
print (str.title())
以上实例输出结果如下：

This Is String Example From Runoob....Wow!!!
请注意，非字母后的第一个字母将转换为大写字母：

实例(Python 3.0+)
#!/usr/bin/python3
 
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)
输出结果为：

Hello B2B2B2 And 3G3G3G
'''

'''
描述
translate() 方法根据参数 table 给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。

语法
translate()方法语法：

str.translate(table)
bytes.translate(table[, delete])    
bytearray.translate(table[, delete]) 
参数
table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
deletechars -- 字符串中要过滤的字符列表。
返回值
返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。

实例
以下实例展示了 translate() 函数的使用方法：

实例(Python 3.0+)
#!/usr/bin/python3
 
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
 
str = "this is string example....wow!!!"
print (str.translate(trantab))
以上实例输出结果如下：

th3s 3s str3ng 2x1mpl2....w4w!!!
以下实例演示如何过滤掉的字符 o：

实例(Python 3.0+)
#!/usr/bin/python
 
# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
 
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
以上实例输出结果：

b'RUNB'
'''

'''
描述
Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

语法
zfill()方法语法：

str.zfill(width)
参数
width -- 指定字符串的长度。原字符串右对齐，前面填充0。
返回值
返回指定长度的字符串。

实例
以下实例展示了 zfill()函数的使用方法：

#!/usr/bin/python3

str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))
以上实例输出结果如下：

str.zfill :  this is string example from runoob....wow!!!
str.zfill :  000000this is string example from runoob....wow!!!

'''

'''
描述
isdecimal() 方法检查字符串是否只包含十进制字符。

语法
isdecimal() 方法语法：

str.isdecimal()
参数
无
返回值
True - 如果字符串中的所有字符都是十进制字符。
False - 至少一个字符不是十进制字符。
实例
以下实例展示了 isdecimal() 函数的使用方法：

实例
#!/usr/bin/python3

str = "runoob2016"
print (str.isdecimal())

str = "23443434"
print (str.isdecimal())
以上实例输出结果如下：

False
True
'''