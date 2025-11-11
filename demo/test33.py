#!/usr/bin/python3

'''
Python3 File(文件) 方法
open() 方法
Python open() 方法用于打开一个文件，并返回文件对象。

在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

open(file, mode='r')
完整的语法格式为：

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
mode 参数有：

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（Python 3 不支持）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
默认为文本模式，如果要以二进制模式打开，加上 b 。

file 对象
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

序号	方法及描述
1	
file.close()

关闭文件。关闭后文件不能再进行读写操作。

2	
file.flush()

刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3	
file.fileno()

返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4	
file.isatty()

如果文件连接到一个终端设备返回 True，否则返回 False。

5	
file.next()

Python 3 中的 File 对象不支持 next() 方法。

返回文件下一行。

6	
file.read([size])

从文件读取指定的字节数，如果未给定或为负则读取所有。

7	
file.readline([size])

读取整行，包括 "\n" 字符。

8	
file.readlines([sizeint])

读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9	
file.seek(offset[, whence])

移动文件读取指针到指定位置

10	
file.tell()

返回文件当前位置。

11	
file.truncate([size])

从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。

12	
file.write(str)

将字符串写入文件，返回的是写入的字符长度。

13	
file.writelines(sequence)

向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''

'''
flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。

一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。

语法
flush() 方法语法如下：

fileObject.flush();
参数
无

返回值
该方法没有返回值。

实例
以下实例演示了 flush() 方法的使用：
'''
# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

# 刷新缓冲区
fo.flush()

# 关闭文件
fo.close()
'''
文件名为:  runoob.txt
'''

'''
fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。

语法
fileno() 方法语法如下：

fileObject.fileno(); 
参数
无

返回值
返回文件描述符。

实例
以下实例演示了 fileno() 方法的使用：
'''
# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

fid = fo.fileno()
print ("文件描述符为: ", fid)

# 关闭文件
fo.close()

'''
文件名为:  runoob.txt
文件描述符为:  3
'''

'''
isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。

语法
isatty() 方法语法如下：

fileObject.isatty(); 
参数
无

返回值
如果连接到一个终端设备返回 True，否则返回 False。

实例
以下实例演示了 isatty() 方法的使用：

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

ret = fo.isatty()
print ("返回值 : ", ret)

# 关闭文件
fo.close()
以上实例输出结果为：

文件名为:  runoob.txt
返回值 :  False
'''
# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

ret = fo.isatty()
print ("返回值 : ", ret) # 返回值 :  False

# 关闭文件
fo.close()


'''
Python 3 的内置函数 next() 通过迭代器调用 __next__() 方法返回下一项。 在循环中，next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration

语法
next() 方法语法如下：

next(iterator[,default])
参数
无

返回值
返回文件下一行。
'''

# 打开文件
fo = open("runoob2.txt", "r",encoding='utf-8')
print ("文件名为: ", fo.name)

for index in range(5):
    line = next(fo)
    print ("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()

'''
结果：
第 0 行 - 这是第一行

第 1 行 - 这是第二行

第 2 行 - 这是第三行

第 3 行 - 这是第四行

第 4 行 - 这是第五行
'''


'''
概述
truncate() 方法用于从文件的首行首字节开始截断，截断文件为 size 个字节，无 size 表示从当前位置截断；截断之后 V 后面的所有字节被删除，其中 Widnows 系统下的换行代表2个字节大小。 。

语法
truncate() 方法语法如下：

fileObject.truncate( [ size ])
参数
size -- 可选，如果存在则文件截断为 size 字节。

返回值
该方法没有返回值。

实例
以下实例演示了 truncate() 方法的使用：

文件 runoob.txt 的内容如下：

1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
循环读取文件的内容：

#!/usr/bin/python3

fo = open("runoob.txt", "r+")
print ("文件名: ", fo.name)

line = fo.readline()
print ("读取行: %s" % (line))

fo.truncate()
line = fo.readlines()
print ("读取行: %s" % (line))

# 关闭文件
fo.close()
以上实例输出结果为：

文件名:  runoob.txt
读取行: 1:www.runoob.com

读取行: ['2:www.runoob.com\n', '3:www.runoob.com\n', '4:www.runoob.com\n', '5:www.runoob.com\n']
以下实例截取 runoob.txt 文件的10个字节：

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)

# 截取10个字节
fo.truncate(10)

str = fo.read()
print ("读取数据: %s" % (str))

# 关闭文件
fo.close()
以上实例输出结果为：

文件名为:  runoob.txt
读取数据: 1:www.runo
'''
def truncate_test1():
    fo = open("runoob3.txt", "r+")
    print ("文件名: ", fo.name)

    line = fo.readline()
    print ("读取行: %s" % (line))

    fo.truncate()
    line = fo.readlines()
    print ("读取行: %s" % (line))

    # 关闭文件
    fo.close()

# truncate_test1()

def truncate_test2():
    # 打开文件
    fo = open("runoob3.txt", "r+")
    print ("文件名为: ", fo.name)

    # 截取10个字节
    fo.truncate(10)

    str = fo.read()
    print ("读取数据: %s" % (str))

    # 关闭文件
    fo.close()

# truncate_test2()

'''
writelines() 是 Python 中文件对象的一个方法，用于将一个字符串列表（或任何可迭代对象）写入文件。

与 write() 方法不同，writelines() 可以一次性写入多行内容，但不会自动添加换行符。

换行需要制定换行符 \n。

语法
writelines() 方法语法如下：

fileObject.writelines( [ sequence ])
参数
fileObject：文件对象，通常通过 open() 函数打开文件后获得。

sequence：一个可迭代对象（如列表、元组等），其中的每个元素都必须是字符串。

返回值：无返回值（返回 None）。

writelines() 方法将可迭代对象中的所有字符串依次写入文件。写入的位置取决于文件的当前指针位置：

如果文件是以追加模式（"a" 或 "a+"）打开的，写入的内容会添加到文件末尾。

如果文件是以读写模式（"r+" 或 "w+"）打开的，写入的内容会从当前文件指针的位置开始覆盖原有内容。

返回值
该方法没有返回值。

实例
以下实例演示了 writelines() 方法的使用：

实例
#!/usr/bin/python3

# 使用 with 语句打开文件，确保文件正确关闭
with open("test.txt", "w") as fo:
    print("文件名为: ", fo.name)
    seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
    fo.writelines(seq)
以上实例输出结果为：

文件名为:  test.txt
查看文件内容：

$ cat test.txt 
菜鸟教程 1
菜鸟教程 2
注意事项
不会自动添加换行符：

writelines() 不会在每行末尾自动添加换行符。如果需要换行，必须在每个字符串中显式添加 \n。

文件模式：

如果文件以只读模式（"r"）打开，调用 writelines() 会抛出 io.UnsupportedOperation 异常。

如果文件以写入模式（"w" 或 "w+"）打开，文件内容会被清空，然后写入新内容。

如果文件以追加模式（"a" 或 "a+"）打开，写入的内容会添加到文件末尾。

文件指针：

写入操作从当前文件指针的位置开始。如果需要从文件开头或特定位置写入，可以使用 seek() 方法移动文件指针。

可迭代对象：

sequence 可以是任何可迭代对象（如列表、元组、生成器等），但其中的每个元素都必须是字符串。
'''
with open('test.txt','w',encoding='utf-8') as f:
    print('filename:',f.name)
    seq = ['菜鸟教程1 \n','菜鸟教程2']
    f.writelines(seq)
