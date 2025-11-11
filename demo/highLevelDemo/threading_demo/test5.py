#!/usr/bin/python3

import threading
# 2. 使用锁保护共享资源
lock = threading.Lock()
count = 0

def workerInc():
    global count
    with lock: # 自动获取和释放锁
        count += 1

threads = [threading.Thread(target=workerInc) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(count) # 输出 10

'''
先把两段写法对比一次就明白为什么必须**「先全部 start，再全部 join」**。
❌ 错误写法：逐个 start + 立即 join

for t in threads:
    t.start()
    t.join()          # 立刻阻塞

执行流程：
启动线程 0 → 主线程阻塞直到 0 结束
启动线程 1 → 主线程阻塞直到 1 结束
...
结果：10 个线程完全串行，并发失效，效率跟单线程一样。
✅ 正确写法：两轮循环

for t in threads:
    t.start()         # 只负责点火，不阻塞
for t in threads:
    t.join()          # 等所有线程一起跑完

第一轮：10 个线程几乎同时启动，真正并发/并行。
第二轮：主线程一次性等待它们全部结束，再往下走。
一句话总结
start() 只是点火，join() 才是等待完工；
先全部点火再一起等，才能保证 并发效果 和 逻辑正确性。
'''