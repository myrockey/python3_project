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


# 生产者慢，消费者快的 错误示例，去掉 producer_thread.join()
def thread_queue_test_slow_producer2():
    q = queue.Queue()

    def producer():
        for i in range(5):
            print(f"[{time.strftime('%H:%M:%S')}] 生产 {i}")
            q.put(i)
            time.sleep(3)  # 生产者快

    def consumer():
        while True:
            item = q.get()
            if item is None:
                print(f"[{time.strftime('%H:%M:%S')}] 消费者收到 None，准备退出")
                break
            print(f"[{time.strftime('%H:%M:%S')}] 消费 {item}")
            time.sleep(0.5)  # 消费者慢
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    # producer_thread.join()  # 等生产者放完  # ❌ 关键一句被去掉了
    q.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


# thread_queue_test_slow_producer2()
'''
输出：
[10:22:22] 生产 0
[10:22:22] 消费 0
[10:22:22] 主线程：准备放入 None
[10:22:22] 消费者收到 None，准备退出
[10:22:22] 主线程：正常退出
[10:22:25] 生产 1
[10:22:28] 生产 2
[10:22:31] 生产 3
[10:22:34] 生产 4

由于去掉了producer_thread.join()，导致还未等生产者放完数据，消费者消费又快，直接q.join()==0,主线程直接放入None,消费者消费完成退出，主线程正常退出
'''