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


# 生产者快，消费者慢的 错误示例，去掉 consumer_thread.join()
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

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()  # 等生产者放完
    q.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    # consumer_thread.join() # ❌ 关键一句被去掉了
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


thread_queue_test_slow_consumer2()
'''
输出：
[10:33:07] 生产 0
[10:33:07] 消费 0
[10:33:07] 生产 1
[10:33:07] 生产 2
[10:33:07] 生产 3
[10:33:07] 生产 4
[10:33:10] 消费 1
[10:33:13] 消费 2
[10:33:16] 消费 3
[10:33:19] 消费 4
[10:33:22] 主线程：准备放入 None
[10:33:22] 主线程：正常退出
[10:33:22] 消费者收到 None，准备退出

去掉consumer_thread.join()导致
主线程提前宣布“我完了”，而后台线程仍在跑，调试日志看上去“顺序错乱”/“提前返回”，
在更复杂的代码里就可能导致：
资源过早释放（关文件、断连接）
日志不完整
单元测试误判“任务已结束”
'''