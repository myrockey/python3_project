#!/usr/bin/python3

import pickle,os

# 序列化
def serialize():
    # 创建1个python对象
    data = {
        'name':'alice',
        'age':19,
        'hobbies': ['reading','traveling']
    }

    # 将对象序列化并保存到文件
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data.pkl','wb') as file:
        pickle.dump(data,file)

# serialize()

# 反序列化
def unserialize():
    # 从文件中加载并反序列化对象
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/data.pkl','rb') as file:
        data = pickle.load(file)
    print(data)

# unserialize() #{'name': 'alice', 'age': 19, 'hobbies': ['reading', 'traveling']}

'''
'wb' 表示以二进制写模式打开文件。
pickle.dump() 将 data 对象序列化并写入文件。

'rb' 表示以二进制读模式打开文件。
pickle.load() 从文件中读取字节流并反序列化为 Python 对象。
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getstate__(self):
        # 自定义序列化逻辑
        return {'name':self.name,'age':self.age}
    
    def __setstate__(self,state):
        # 自定义反序列化逻辑
        self.name = state['name']
        self.age = state['age']

# 创建对象并序列化
person = Person('bob',30)
def serialize2file(data,filename):
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/' + filename,'wb') as file:
        pickle.dump(data,file)

# serialize2file(person,'person.pkl')

#反序列化对象
def unserializeFromfile(filename):
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/' + filename,'rb') as file:
        data = pickle.load(file)
    print(data.name,data.age)

# unserializeFromfile('person.pkl') # bob 30


data = {'name': 'Alice', 'age': 25}
filename = 'data2.pkl'
def serialize2file2(data,filename,protocol=pickle.HIGHEST_PROTOCOL):
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/' + filename, 'wb') as f:
        pickle.dump(data, f, protocol)

# serialize2file2(data,filename)

#反序列化对象
def unserializeFromfile2(filename):
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    with open(exec_path + '/' + filename,'rb') as file:
        data = pickle.load(file)
    print(data)

# unserializeFromfile2(filename)

# 序列化为字节串（网络传输/缓存）
bytes_data = pickle.dumps([1, 2, 3], protocol=4)
restored_list = pickle.loads(bytes_data)
print(bytes_data)
print(restored_list)

'''
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
[1, 2, 3]
'''