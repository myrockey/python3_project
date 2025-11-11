#!/usr/bin/python3

'''
Python 装饰器
装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。

装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。



装饰器的语法使用 @decorator_name 来应用在函数或方法上。

Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

装饰器的应用场景：

日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
性能分析: 可以使用装饰器来测量函数的执行时间。
权限控制: 装饰器可用于限制对某些函数的访问权限。
缓存: 装饰器可用于实现函数结果的缓存，以提高性能。
基本语法
Python 装饰允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。

语法
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
       
        result = original_function(*args, **kwargs)
       
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
       
        return result
    return wrapper

# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现
解析：decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个内部函数 wrapper，在 wrapper 函数内部，你可以执行一些额外的操作，然后调用原始函数 func，并返回其结果。

decorator_function 是装饰器，它接收一个函数 original_function 作为参数。
wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。
当我们使用 @decorator_function 前缀在 target_function 定义前，Python会自动将 target_function 作为参数传递给 decorator_function，然后将返回的 wrapper 函数替换掉原来的 target_function。
使用装饰器
装饰器通过 @ 符号应用在函数定义之前，例如：

@time_logger
def target_function():
    pass
等同于：

def target_function():
    pass
target_function = time_logger(target_function)
这会将 target_function 函数传递给 decorator 装饰器，并将返回的函数重新赋值给 target_function。从而，每次调用 target_function 时，实际上是调用了经过装饰器处理后的函数。

通过装饰器，开发者可以在保持代码整洁的同时，灵活且高效地扩展程序的功能。

以下是一个简单的装饰器示例，它会在函数执行前后打印日志：

实例
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
输出：

在原函数之前执行
Hello!
在原函数之后执行
my_decorator 是一个装饰器函数，它接受 say_hello 作为参数，并返回 wrapper 函数。
@my_decorator 将 say_hello 替换为 wrapper。
带参数的装饰器
如果原函数需要参数，可以在装饰器的 wrapper 函数中传递参数：

实例
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
以上代码代码定义了一个装饰器 my_decorator，它会在被装饰的函数执行前后分别打印一条消息。装饰器通过 wrapper 函数包裹原函数，并在调用原函数前后添加额外操作。

输出：

在原函数之前执行
Hello, Alice!
在原函数之后执行
装饰器本身也可以接受参数，此时需要额外定义一个外层函数：

实例
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。decorator 接受一个函数 func，并返回一个 wrapper 函数。wrapper 函数会调用 func 函数 num_times 次。使用 @repeat(3) 装饰s ay_hell 函数后，调用 say_hello 会打印 "Hello!" 三次。



Hello!
Hello!
Hello!
类装饰器
除了函数装饰器，Python 还支持类装饰器。

类装饰器（Class Decorator）是一种用于动态修改类行为的装饰器，它接收一个类作为参数，并返回一个新的类或修改后的类。

类装饰器可以用于：

添加/修改类的方法或属性

拦截实例化过程
实现单例模式、日志记录、权限检查等功能

类装饰器有两种常见形式：

函数形式的类装饰器（接收类作为参数，返回新类）
类形式的类装饰器（实现 __call__ 方法，使其可调用）
函数形式的类装饰器
以下实例给类添加日志功能：

实例
def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类
       
        def __getattr__(self, name):
            """拦截未定义的属性访问，转发给原始类"""
            return getattr(self.wrapped, name)
       
        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")
   
    return Wrapper  # 返回包装后的类

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display()
输出：

调用 MyClass.display() 前
这是 MyClass 的 display 方法
调用 MyClass.display() 后
类形式的类装饰器（实现 __call__ 方法）
以下实例实现单例模式（Singleton）：

实例
class SingletonDecorator:
    """类装饰器，使目标类变成单例模式"""
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
   
    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True，说明是同一个实例
输出：

Database 初始化
True
内置装饰器
Python 提供了一些内置的装饰器，例如：

@staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。

@classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）。

@property: 将方法转换为属性，使其可以像属性一样访问。

实例
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)
多个装饰器的堆叠
你可以将多个装饰器堆叠在一起，它们会按照从下到上的顺序依次应用。例如：

实例
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
输出：

Decorator 1
Decorator 2
Hello!
'''
def my_decorator(func):
    def wrapper2():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper2

@my_decorator
def say_hello():
    print("hello!")

say_hello()

'''
输出：

在原函数之前执行
Hello!
在原函数之后执行
my_decorator 是一个装饰器函数，它接受 say_hello 作为参数，并返回 wrapper 函数。
@my_decorator 将 say_hello 替换为 wrapper。
'''

# 带参数的装饰器
def my_decorator2(func):
    def wrapper(*args,**kwargs):
        print("在原函数之前执行")
        func(*args,**kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator2
def greet(name):
    print(f'hello,{name}!')

greet('Alice')

# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数：
def repeat2(num_times):
    def my_decorator2(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return my_decorator2

@repeat2(3)
def say_hello(name):
    print(f"hello,{name}!")

say_hello('rockey')
'''
hello,rockey!
hello,rockey!
hello,rockey!
repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。decorator 接受一个函数 func，并返回一个 wrapper 函数。wrapper 函数会调用 func 函数 num_times 次。使用 @repeat(3) 装饰s ay_hell 函数后，调用 say_hello 会打印 "Hello!" 三次。
'''

# 函数形式的类装饰器
# 以下实例给类添加日志功能：
def log_class(cls):
    '''类装饰器，在调用方法前后打印日志'''
    class wrapper:
        def __init__(self,*args,**kwargs):
            self.wrapped = cls(*args,**kwargs) # 实例化原始类
        
        def __getattr__(self,name):
            '''拦截未定义的属性访问，转发给原始类'''
            return getattr(self.wrapped,name)
        
        def display2(self):
            print(f"调用{cls.__name__}.display2() 前")
            self.wrapped.display2()
            print(f"调用{cls.__name__}.display2() 后")
    return wrapper # 返回包装后的类

@log_class
class MyClass:
    def display2(self):
        print("这是Myclass的display2方法")

obj = MyClass()
obj.display2()
obj.name2 = 'he'
print(obj.name2)

class MyClass2:
    def display2(self):
        print("这是Myclass2的display2方法")

obj2 = MyClass2()
obj2.display2()
obj2.name2 = 'qw'
print(obj2.name2)

'''
结果：
调用MyClass.display2() 前
这是Myclass的display2方法
调用MyClass.display2() 后
he
这是Myclass2的display2方法
qw
'''

# 类形式的类装饰器（实现 __call__ 方法）
# 以下实例实现单例模式（Singleton）：
class SingleExampleDecorator:
    '''类装饰器，使目标变成单例模式'''
    def __init__(self,cls):
        self.cls = cls
        self.instance = None
    
    def __call__(self, *args, **kwds):
        '''拦截实例化过程，确保只创建1个实例'''
        if self.instance is None:
            self.instance = self.cls(*args,**kwds)
        return self.instance
    
@SingleExampleDecorator
class MyDatabase:
    def __init__(self):
        print("Database 初始化")

db1 = MyDatabase()
db2 = MyDatabase()
print(db1 is db2) # True，说明是同1个实例
'''
输出：

Database 初始化
True
'''

# 内置装饰器
'''
Python 提供了一些内置的装饰器，例如：

@staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。

@classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）。

@property: 将方法转换为属性，使其可以像属性一样访问。
'''
class MyClass2:
    @staticmethod
    def static_method():
        print("this is a static method")
    
    @classmethod
    def class_method(cls):
        print(f"this is a class method of {cls.__name__}.")
    
    @property
    def name2(self):
        return self._name1
    
    @name2.setter
    def name2(self,value):
        self._name1 = value

MyClass2.static_method()
MyClass2.class_method()

obj = MyClass2()
obj.name2 = "ALice"
print(obj._name1) # 调用类属性 _name1
print(obj.name2)  # 调用类方法 name2

'''
this is a static method
this is a class method of MyClass2.
ALice
ALice
'''

# 多个装饰器的堆叠
def decorator1(func):
    def wrapper():
        print('decorator 1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator 2')
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print('hello')

say_hello()

'''
结果：
decorator 1
decorator 2
hello
'''
