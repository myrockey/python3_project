#!/usr/bin/python3

# 4. 生产者-消费者模型（Condition）
#!/usr/bin/python3
import threading, time, random
from collections import deque

queue = deque()
cond   = threading.Condition()
MAX_ITEMS = 5

def producer():
    for i in range(10):
        with cond:
            while len(queue) >= MAX_ITEMS:
                cond.wait()
            queue.append(i)
            print(f"[{threading.current_thread().name}] Produced {i}")
            cond.notify()
        time.sleep(random.uniform(0.1, 0.3))

def consumer():
    for _ in range(10):
        with cond:
            while not queue:
                cond.wait()
            item = queue.popleft()
            print(f"[{threading.current_thread().name}] Consumed {item}")
            cond.notify()
        time.sleep(random.uniform(0.1, 0.3))

t1 = threading.Thread(target=producer, name='Producer')
t2 = threading.Thread(target=consumer, name='Consumer')
t1.start()
t2.start()
t1.join()
t2.join()
print('All tasks finished')

'''
输出：
[Producer] Produced 0
[Consumer] Consumed 0
[Producer] Produced 1
[Consumer] Consumed 1
[Producer] Produced 2
[Consumer] Consumed 2
[Producer] Produced 3
[Consumer] Consumed 3
[Producer] Produced 4
[Producer] Produced 5
[Consumer] Consumed 4
[Consumer] Consumed 5
[Producer] Produced 6
[Consumer] Consumed 6
[Producer] Produced 7
[Consumer] Consumed 7
[Producer] Produced 8
[Producer] Produced 9
[Consumer] Consumed 8
[Consumer] Consumed 9
All tasks finished


这段代码是一个手写的“生产者-消费者”并发模型，用 Python 的 threading.Condition 实现线程间安全通信与阻塞唤醒。逐行含义如下：
① 工具与初始状态
Python
复制
queue = deque()              # 共享队列，存放产品
cond  = threading.Condition() # 条件变量，用于线程等待/通知
MAX_ITEMS = 5                # 队列上限，满时阻塞生产者
② 生产者线程逻辑
Python
复制
def producer():
    for i in range(10):               # 共生产 10 件产品
        with cond:                    # 1. 拿到条件锁
            while len(queue) >= MAX_ITEMS:  # 2. 队列满 → 自旋等待
                cond.wait()            #    释放锁并阻塞，直到被 notify
            queue.append(i)            # 3. 有空位，放入产品
            print(f"[...] Produced {i}")
            cond.notify()              # 4. 唤醒**一个**正在 wait 的线程（通常是消费者）
        time.sleep(random.uniform(0.1, 0.3))  # 5. 模拟生产耗时（**已释放锁**）
关键点
wait() 会原子地释放锁并阻塞；被 notify 后重新抢锁再返回。
notify() 只唤醒一个等待线程，减少“惊群”。
③ 消费者线程逻辑
Python
复制
def consumer():
    for _ in range(10):           # 共消费 10 次
        with cond:                # 1. 拿锁
            while not queue:      # 2. 队列空 → 等待
                cond.wait()
            item = queue.popleft() # 3. 取出产品
            print(f"[...] Consumed {item}")
            cond.notify()         # 4. 唤醒等待者（通常是生产者）
        time.sleep(random.uniform(0.1, 0.3))  # 5. 模拟消费耗时（**已释放锁**）
④ 启动与同步
Python
复制
t1 = threading.Thread(target=producer, name='Producer')
t2 = threading.Thread(target=consumer, name='Consumer')
t1.start(); t2.start()   # 并发开始
t1.join(); t2.join()     # 主线程等待两者都结束
print('All tasks finished')
运行流程图（单步视角）
复制
主线程
├─ t1 抢到锁 → 队列空 → 放 0 → notify → 睡
├─ t2 抢到锁 → 取 0 → notify → 睡
└─ ... 重复 10 轮
等 t1、t2 结束 → 打印 All tasks finished
一句话总结
生产者满则等，消费者空则等；
通过 Condition 的 wait/notify 实现线程安全、阻塞式的生产-消费流水线。
'''