#!/usr/bin/python3

import threading,queue

"""
3. 线程间通信
线程间通信可以通过队列（Queue）来实现。Queue 是线程安全的，可以在多个线程之间安全地传递数据。
"""
def worker(q):
    while not q.empty():
        item = q.get()
        print(f"处理项目：{item}")
        q.task_done()

# 创建1个队列并填充数据
q = queue.Queue()
for i in range(10):
    q.put(i)

# 创建线程实例
thread1 = threading.Thread(target=worker,args=(q,))
thread2 = threading.Thread(target=worker,args=(q,))
# 启动线程
thread1.start()
thread2.start()
# 等待队列中的所有项目被处理完毕
q.join()
print('所有项目处理完毕')
