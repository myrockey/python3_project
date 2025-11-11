#!/usr/bin/python3

import queue
import threading
import time

# 生产者快，消费者慢的 正常示例
def thread_queue_test_slow_consumer():
    q = queue.Queue()

    def producer():
        for i in range(5):
            print(f"[{time.strftime('%H:%M:%S')}] 生产 {i}")
            q.put(i)
            time.sleep(0.1)  # 生产者快

    def consumer():
        while True:
            item = q.get()
            if item is None:
                print(f"[{time.strftime('%H:%M:%S')}] 消费者收到 None，准备退出")
                break
            print(f"[{time.strftime('%H:%M:%S')}] 消费 {item}")
            time.sleep(3)  # 消费者慢
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()  # 等生产者放完
    q.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


# thread_queue_test_slow_consumer()
'''
输出：
[09:52:07] 生产 0
[09:52:07] 消费 0
[09:52:08] 生产 1
[09:52:08] 生产 2
[09:52:08] 生产 3
[09:52:08] 生产 4
[09:52:10] 消费 1
[09:52:13] 消费 2
[09:52:16] 消费 3
[09:52:19] 消费 4
[09:52:22] 主线程：准备放入 None
[09:52:22] 消费者收到 None，准备退出
[09:52:22] 主线程：正常退出

这就保证了，只有消费者完全消费完成后，主线程才会执行 q.join()之后的代码
'''


# 生产者快，消费者慢的 错误示例，去掉 producer_thread.start()
def thread_queue_test_slow_consumer2():
    q = queue.Queue()

    def producer():
        for i in range(5):
            print(f"[{time.strftime('%H:%M:%S')}] 生产 {i}")
            q.put(i)
            time.sleep(0.1)  # 生产者快

    def consumer():
        while True:
            item = q.get()
            if item is None:
                print(f"[{time.strftime('%H:%M:%S')}] 消费者收到 None，准备退出")
                break
            print(f"[{time.strftime('%H:%M:%S')}] 消费 {item}")
            time.sleep(3)  # 消费者慢
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # producer_thread.start() # ❌ 关键一句被去掉了
    consumer_thread.start()

    producer_thread.join()  # 等生产者放完
    q.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


# thread_queue_test_slow_consumer2()


# 输出：
# Traceback (most recent call last):
#   File "d:\projects\python3_project\demo\highLevelDemo\queue_demo\thread_queue_test4.py", line 96, in <module>
#     thread_queue_test_slow_consumer2()
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
#   File "d:\projects\python3_project\demo\highLevelDemo\queue_demo\thread_queue_test4.py", line 88, in thread_queue_test_slow_consumer2
#     producer_thread.join()  # 等生产者放完
#     ~~~~~~~~~~~~~~~~~~~~^^
#   File "D:\Program Files\Python313\Lib\threading.py", line 1085, in join
#     raise RuntimeError("cannot join thread before it is started")
# RuntimeError: cannot join thread before it is started

# 结论：
# producer_thread.start() 必须开启，否则报错



# 生产者快，消费者慢的 错误示例，去掉 consumer_thread.start()
def thread_queue_test_slow_consumer3():
    q = queue.Queue()

    def producer():
        for i in range(5):
            print(f"[{time.strftime('%H:%M:%S')}] 生产 {i}")
            q.put(i)
            time.sleep(0.1)  # 生产者快

    def consumer():
        while True:
            item = q.get()
            if item is None:
                print(f"[{time.strftime('%H:%M:%S')}] 消费者收到 None，准备退出")
                break
            print(f"[{time.strftime('%H:%M:%S')}] 消费 {item}")
            time.sleep(3)  # 消费者慢
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start() 
    # consumer_thread.start() # ❌ 关键一句被去掉了

    producer_thread.join()  # 等生产者放完
    q.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


thread_queue_test_slow_consumer3()

"""
输出：
[10:15:50] 生产 0
[10:15:50] 生产 1
[10:15:50] 生产 2
[10:15:50] 生产 3
[10:15:50] 生产 4

由于没有consumer_thread.start() 导致，主线程卡死，消费者未能正常运行。
"""

