#!/usr/bin/python3

# 3.事件同步
import threading,time

event = threading.Event()

def taskWaiter():
    print("waiting for event...")
    event.wait()
    print("event triggered!")

t = threading.Thread(target=taskWaiter)
t.start()

# 主线程触发事件
time.sleep(2) # 模拟延迟
event.set()

t.join()

'''
输出：
waiting for event...
event triggered!

这段代码的本意是：
子线程先阻塞，等主线程 2 秒后“发信号”再继续执行。
'''