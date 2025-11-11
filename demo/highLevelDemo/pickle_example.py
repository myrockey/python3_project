'''
Python Pickle 模块
Python 的 pickle 模块是一个用于序列化和反序列化 Python 对象的标准库模块。

序列化是指将 Python 对象转换为字节流的过程，而反序列化则是将字节流转换回 Python 对象的过程。

pickle 模块可以将几乎所有的 Python 对象（如列表、字典、类实例等）保存到文件中，或者通过网络传输，然后在需要时重新加载。

为什么使用 Pickle 模块？
数据持久化：将 Python 对象保存到文件中，以便在程序关闭后仍然可以访问这些数据。
数据传输：通过网络传输 Python 对象，例如在分布式系统中传递数据。
快速存储和加载：pickle 模块可以高效地处理复杂的数据结构，适合需要快速存储和加载的场景。
Pickle 模块的基本用法
1. 序列化对象
使用 pickle.dump() 方法可以将 Python 对象序列化并保存到文件中。

实例
import pickle

# 创建一个 Python 对象
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'traveling']
}

# 将对象序列化并保存到文件
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
'wb' 表示以二进制写模式打开文件。
pickle.dump() 将 data 对象序列化并写入文件。
2. 反序列化对象
使用 pickle.load() 方法可以从文件中加载并反序列化 Python 对象。

实例
import pickle

# 从文件中加载并反序列化对象
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
'rb' 表示以二进制读模式打开文件。
pickle.load() 从文件中读取字节流并反序列化为 Python 对象。
Pickle 模块的注意事项
安全性：pickle 模块在反序列化时会执行任意代码，因此不要加载来自不可信来源的 pickle 数据，以免遭受恶意攻击。
兼容性：pickle 生成的字节流是 Python 特有的，不同版本的 Python 之间可能存在兼容性问题。
性能：对于大型数据集，pickle 的序列化和反序列化可能会比较慢，可以考虑使用更高效的序列化工具，如 json 或 msgpack。
高级用法：自定义对象的序列化
pickle 模块支持自定义类的序列化。默认情况下，pickle 会保存对象的属性和类名。如果需要更复杂的序列化逻辑，可以在类中实现 __getstate__() 和 __setstate__() 方法。

实例
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getstate__(self):
        # 自定义序列化逻辑
        return {'name': self.name, 'age': self.age}

    def __setstate__(self, state):
        # 自定义反序列化逻辑
        self.name = state['name']
        self.age = state['age']

# 创建对象并序列化
person = Person('Bob', 30)
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# 反序列化对象
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)

print(loaded_person.name, loaded_person.age)
pickle 模块常用方法
方法	说明	示例
pickle.dump(obj, file)	将对象序列化并写入文件	pickle.dump(data, open('data.pkl', 'wb'))
pickle.load(file)	从文件读取并反序列化对象	data = pickle.load(open('data.pkl', 'rb'))
pickle.dumps(obj)	将对象序列化为字节串	bytes_data = pickle.dumps([1, 2, 3])
pickle.loads(bytes)	从字节串反序列化对象	lst = pickle.loads(bytes_data)
pickle.HIGHEST_PROTOCOL	可用的最高协议版本（属性）	pickle.dump(..., protocol=pickle.HIGHEST_PROTOCOL)
pickle.DEFAULT_PROTOCOL	默认协议版本（属性，通常为4）	pickle.dumps(obj, protocol=pickle.DEFAULT_PROTOCOL)
1. 序列化对象到文件

实例
import pickle
data = {'name': 'Alice', 'age': 25}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
2. 从文件反序列化

实例
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
print(loaded_data)  # 输出: {'name': 'Alice', 'age': 25}
3. 序列化为字节串（网络传输/缓存）

实例
bytes_data = pickle.dumps([1, 2, 3], protocol=4)
restored_list = pickle.loads(bytes_data)
pickle 模块协议版本
协议版本	说明
0	人类可读的ASCII格式（兼容旧版）
1	二进制格式（兼容旧版）
2	Python 2.3+ 优化支持类对象
3	Python 3.0+ 默认协议（不支持Python 2）
4	Python 3.4+ 支持更大对象和更多数据类型
5	Python 3.8+ 支持内存优化和数据共享

'''