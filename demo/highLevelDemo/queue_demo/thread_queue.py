#!/usr/bin/python3

import queue
import threading
import time

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
'''
put() → 计数器 +1
task_done() → 计数器 -1
join() → 阻塞到计数器 == 0

这三个方法必须成对使用，否则程序会卡死。一句话记忆：
生产者 put() 后，消费者 task_done()；
主线程 join() 等着看 所有任务是否都被标记完成。
1. q.task_done()
由消费者线程调用，表示“我刚从队列里 get() 出来的那个任务已经处理完了”。
每调一次，队列内部 未完成任务计数器 -1。
如果你 get() 了 3 次却只 task_done() 2 次，计数器永远不为 0 → join() 永远阻塞。
2. q.join()
由主线程（或任意需要等待的线程）调用，阻塞直到计数器变为 0。
计数器为 0 意味着：所有曾经被 put() 进去的任务，都被对应的 task_done() 标记完成了。
'''

'''
producer_thread.start()   # 1. 启动生产者线程（开始往队列放数据）
producer_thread.join()    # 2. 主线程阻塞，直到**生产者**把5个put全部执行完
consumer_thread.start()   # 3. 启动消费者线程（开始从队列拿数据）
consumer_thread.join()    # 4. 主线程阻塞，直到**消费者**收到None后break并退出
能否去掉？
1 和 3（start()）绝对不能省
否则对应线程根本不会运行。
2 和 4（join()）可以省，但后果不同：
表格
复制
去掉哪句	后果
去掉 producer_thread.join()	主线程可能提前把 None 塞进队列，导致消费者提前退出，漏掉后面还没生产完的数据。
去掉 consumer_thread.join()	主线程会在发送 None 之后立刻继续往下走（或直接结束），可能看不到消费者打印的最后几行，甚至进程直接退出。
最小可靠写法（保持顺序 & 不丢数据）

producer_thread.start()
consumer_thread.start()   # 先让两端都跑起来
producer_thread.join()    # 等生产完毕
q.put(None)               # 再发结束信号
consumer_thread.join()    # 等消费者真正结束
'''

'''
当注释掉:producer_thread.join()
输出:
生产 0
消费 0
主线程：准备放入 None
生产 1
生产 2
生产 3
生产 4
主线程：正常退出

主线程退出，不会去关闭 生产者线程吗？生产者线程为啥能执行完成
编辑
复制
分享
这是个非常关键的疑问，涉及 Python 线程的底层行为 和 进程生命周期 的问题。
✅ 简短回答
主线程退出时，不会强制杀掉其他线程（包括生产者线程），
只要进程还在，其他线程会继续运行，直到它们自己结束。
🔍 详细解释
✅ 1. Python 线程是 用户级线程（非内核级）
Python 的线程是由 操作系统调度 的；
但 主线程退出不会自动杀掉其他线程；
只有所有非守护线程都结束后，进程才会真正退出。
✅ 2. 你的生产者线程是 非守护线程
默认情况下，threading.Thread() 创建的线程是 非守护线程；
所以即使主线程执行完了，只要生产者线程还在运行，进程就不会退出；
生产者线程会继续执行完它的 for i in range(5)。
✅ 3. 为什么进程没卡住？
虽然你注释了 producer_thread.join()，但：
生产者线程最终会自己结束；
消费者线程也最终会退出（因为收到了 None）；
所有非守护线程都结束后，进程自然退出。
'''