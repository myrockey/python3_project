#!/usr/bin/python3

import threading
# 1. 基础线程创建
def worker(num):
    print(f"worker {num} started")

threads = []
for i in range(3):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

'''
输出：
worker 0 started
worker 1 started
worker 2 started
'''