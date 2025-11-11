#!/usr/bin/python3

# 同一行显示多条语句
# Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：

# 实例(Python 3.0+)
# #!/usr/bin/python3
 
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 使用脚本执行以上代码，输出结果为：

# runoob
# 使用交互式命令行执行，输出结果为：

# >>> import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# runoob
# 7
# 此处的 7 表示字符数，runoob 有 6 个字符，\n 表示一个字符，加起来 7 个字符。

# >>> import sys
# >>> sys.stdout.write(" hi ")    # hi 前后各有 1 个空格
#  hi 4


# 多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。

# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

# 我们将首行及后面的代码组称为一个子句(clause)。

# 如下实例：

# if expression : 
#    suite
# elif expression : 
#    suite 
# else : 
#    suite

# print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x,end="")
print(y,end='')
print() # 可写，可不写


