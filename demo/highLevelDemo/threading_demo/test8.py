#!/usr/bin/python3

# 4. 生产者-消费者模型（Condition）

import threading, time, random
from collections import deque

queue = deque()
cond   = threading.Condition()
MAX_ITEMS = 5

def producer():
    for i in range(10):
        with cond:
            while len(queue) >= MAX_ITEMS:
                print(f"[{threading.current_thread().name}] Produced limit MAX_ITEMS")
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
        time.sleep(random.uniform(1, 3))

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
[Producer] Produced 2
[Producer] Produced 3
[Producer] Produced 4
[Producer] Produced 5
[Consumer] Consumed 1
[Producer] Produced 6
[Consumer] Consumed 2
[Producer] Produced 7
[Consumer] Consumed 3
[Producer] Produced 8
[Consumer] Consumed 4
[Producer] Produced 9
[Consumer] Consumed 5
[Consumer] Consumed 6
[Consumer] Consumed 7
[Consumer] Consumed 8
[Consumer] Consumed 9
All tasks finished
PS D:\projects\python3_project> & "D:/Program Files/Python313/python.exe" d:/projects/python3_project/demo/highLevelDemo/threading_demo/test8.py
[Producer] Produced 0
[Consumer] Consumed 0
[Producer] Produced 1
[Producer] Produced 2
[Producer] Produced 3
[Producer] Produced 4
[Producer] Produced 5
[Producer] Produced limit MAX_ITEMS
[Consumer] Consumed 1
[Producer] Produced 6
[Producer] Produced limit MAX_ITEMS
[Consumer] Consumed 2
[Producer] Produced 7
[Producer] Produced limit MAX_ITEMS
[Consumer] Consumed 3
[Producer] Produced 8
[Producer] Produced limit MAX_ITEMS
[Consumer] Consumed 4
[Producer] Produced 9
[Consumer] Consumed 5
[Consumer] Consumed 6
[Consumer] Consumed 7
[Consumer] Consumed 8
[Consumer] Consumed 9
All tasks finished

和 test7的区别，就在消费者消费慢，生产者队列满了，然后切换为消费者消费

### 一、 直接cond.wait()了，并没有去 cond.notify() , 为啥消费者会自动运行呢？

消费者不是靠「生产者显式 notify() 后才复活」这一条路；
Condition 的底层机制保证了：只要锁被释放，等待者就有机会抢锁继续执行。
拆开看就明白了：
1. 生产者发现队列满时的完整动作
Python
复制
with cond:                   # ① 拿到锁
    while len(queue) >= MAX_ITEMS:
        print(...limit...)
        cond.wait()          # ② **原子地释放锁 + 阻塞自己**
cond.wait() 在阻塞前已经把锁释放了！
因此消费者此刻可以立即抢到锁，继续消费。
2. 消费者消费后的一步
Python
复制
with cond:                   # ③ 消费者拿到锁
    item = queue.popleft()
    cond.notify()            # ④ 唤醒**一个**正在 wait 的线程（通常是生产者）
一旦消费者 popleft() 让队列长度 < MAX_ITEMS，再 notify()，
生产者就从 wait() 返回并重新抢锁，继续生产。
3. 流程图（单轮）
复制
Producer          Consumer
   ├─lock          |
   │ queue满       |
   ├─cond.wait()  ├─lock（立刻抢到，因为锁已被生产者释放）
   │ 阻塞并放锁   ├─popleft()
   │              ├─cond.notify()  → 唤醒生产者
   │              └─unlock
   ├─被唤醒后抢锁 |
   └─继续生产     |
一句话总结
cond.wait() 会释放锁；
只要锁被释放，任何等待者（消费者）都能抢锁运行，不需要额外的 notify() 来“启动”它们。


### 二.那么 消费者 cond.notify() 后，消费者就会自己进入等待吗？

不会！
cond.notify() 只负责唤醒别人，不会让当前线程（消费者）自己进入等待。
1. 消费者代码顺序
Python
复制
with cond:
    while not queue:
        cond.wait()          # 只有这里才会**主动阻塞**
    item = queue.popleft()
    cond.notify()            # 仅仅唤醒**一个**等待者（通常是生产者）
# 离开 with 块才**释放锁**，消费者继续往下执行（sleep、下一轮循环）
2. 流程拆解（单轮）
表格
复制
步骤	消费者状态
抢到锁	运行中
popleft()	运行中
cond.notify()	运行中（只是发个信号）
退出 with	锁释放，但仍继续执行后面的 time.sleep(...)
sleep 结束	进入下一轮循环，再次抢锁
3. 什么时候消费者才会自己阻塞？
只有 再次抢锁后 发现 queue 为空：
Python
复制
while not queue:
    cond.wait()   # 这里才会**释放锁并阻塞自己**
一句话总结
notify() 只叫醒别人，不会让当前线程睡觉；
消费者想阻塞，必须再次抢锁后发现条件不满足，主动调用 wait()。
'''