#!/usr/bin/python3

import queue
import threading
import time

# 正常示例
def thread_queue_test():
    # 创建1个队列
    q = queue.Queue()

    # 生产者线程
    def producer():
        for i in range(5):
            print(f"生产 {i}")
            q.put(i)
            time.sleep(1)

    # 消费者线程
    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"消费 {item}")
            q.task_done()

    # 启动生产者线程
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # 启动消费者线程
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()

    # 等待生产者线程完成
    producer_thread.join()

    # 等待队列中所有任务完成
    q.join()

    # # 发送结束信号，结束消费者线程
    print("主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print("主线程：正常退出")

# thread_queue_test()
'''
输出：

生产 0
消费 0
生产 1
消费 1
生产 2
消费 2
生产 3
消费 3
生产 4
消费 4
主线程：准备放入 None
主线程：正常退出
'''


# 错误示例，去掉 q.join()
def thread_queue_test2():
    # 创建1个队列
    q = queue.Queue()

    # 生产者线程
    def producer():
        for i in range(5):
            print(f"生产 {i}")
            q.put(i)

    # 消费者线程
    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"消费 {item}")
            q.task_done()

    # 启动生产者线程
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # 启动消费者线程
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()

    # 等待生产者线程完成
    producer_thread.join()

    # 等待队列中所有任务完成
    # q.join()

    # # 发送结束信号，结束消费者线程
    print("主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print("主线程：正常退出")

# thread_queue_test2()

'''
去掉 q.join() 后，程序仍然可以“看起来”正常退出，但存在潜在的逻辑缺陷，我们来逐层分析：
✅ 运行结果（表面现象）
生产者会打印 生产 0 到 生产 4；
消费者会打印 消费 0 到 消费 4；
最后打印：

主线程：准备放入 None
主线程：正常退出

没有异常，没有卡死。
❗但问题藏在细节里：
你失去了对“队列中任务是否已处理完”的同步保障。
举个例子：
假设消费者线程偶然卡了一下（比如系统调度延迟），而主线程已经执行了：

producer_thread.join()  # 生产者已经放完数据
q.put(None)             # 主线程立刻放入 None

这时：
消费者还没来得及处理完所有数据；
就已经收到了 None，提前退出；
虽然你看到了“消费 0~4”，但这是因为你没有加延迟或重负载；
在高并发或消费者慢的场景下，可能漏处理任务。
✅ q.join() 的作用
它会阻塞主线程，直到所有 q.put() 进去的任务都被 q.task_done() 标记为完成；
这是 生产者-消费者模型中“任务同步”的关键机制；
没有它，你就失去了“任务是否处理完”的保障。
✅ 正确做法（推荐）


producer_thread.join()  # 等生产者放完数据
q.join()                # 等队列中所有任务被消费完
q.put(None)             # 再通知消费者退出
consumer_thread.join()

✅ 总结一句话
去掉 q.join() 不会立刻崩，但失去了“任务处理完”的同步保障，可能在边界情况下丢任务或提前退出。

面给你一个最小可复现的“消费者慢”版本，
去掉 q.join() 后，消费者会提前收到 None，导致任务没处理完就退出。
'''
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
    # q.join()  # ❌ 关键一句被去掉了
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：准备放入 None")
    q.put(None)
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


# thread_queue_test_slow_consumer()

'''
输出：
[09:42:47] 生产 0
[09:42:47] 消费 0
[09:42:47] 生产 1
[09:42:47] 生产 2
[09:42:48] 生产 3
[09:42:48] 生产 4
[09:42:48] 主线程：准备放入 None
[09:42:50] 消费 1
[09:42:53] 消费 2
[09:42:56] 消费 3
[09:42:59] 消费 4
[09:43:02] 消费者收到 None，准备退出
[09:43:02] 主线程：正常退出

Queue 保证 FIFO，只要 None 被排在队尾，消费者就一定会把前面所有任务处理完；
去掉 q.join() 的真正风险是“时机不确定”，而不是“一定会丢”；
想百分百不丢，仍应在所有任务被标记完成后再 put(None)——也就是加回 q.join()。
'''

# 加回join后，生产者快，消费者慢的 正常示例
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
    consumer_thread.join()
    print(f"[{time.strftime('%H:%M:%S')}] 主线程：正常退出")


thread_queue_test_slow_consumer2()
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
