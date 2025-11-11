#!/usr/bin/python3
import queue

'''
队列类型
1. Queue
Queue 是 queue 模块中最常用的队列类型，它实现了标准的先进先出（FIFO）队列。以下是 Queue 的基本用法：
'''
def queue_test():
    # 创建1个队列(先进先出)
    q = queue.Queue()
    # 入队列
    q.put(1)
    q.put(2)
    q.put(3)

    # 从队列取出
    print(q.get()) # 1
    print(q.get()) # 2
    print(q.get()) # 3

# queue_test()

'''
2. LifoQueue
LifoQueue 是一种后进先出（LIFO）的队列，类似于栈。以下是 LifoQueue 的基本用法：
'''
def LifoQueue_test():
    # 创建1个队列(后进先出) 类似于栈
    q = queue.LifoQueue()
    # 入队列
    q.put(1)
    q.put(2)
    q.put(3)

    # 从队列取出
    print(q.get()) # 3
    print(q.get()) # 2
    print(q.get()) # 1

# LifoQueue_test()

'''
3. PriorityQueue
PriorityQueue 是一种优先级队列，元素按照优先级顺序被取出。以下是 PriorityQueue 的基本用法：
'''
def PriorityQueue_test():
    # 创建1个队列(后进先出) 类似于栈
    q = queue.PriorityQueue()
    # 入队列,元素为元组(优先级，数据)
    q.put((3,'Low data'))
    q.put((1,"High data"))
    q.put((2,"midd data"))

    # 从队列取出
    print(q.get()) 
    print(q.get())
    print(q.get())

# PriorityQueue_test()
'''
输出：
(1, 'High data')
(2, 'midd data')
(3, 'Low data')

优先级越高越先出队列
'''