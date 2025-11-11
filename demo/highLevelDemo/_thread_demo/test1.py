#!/usr/bin/python3

import _thread
import time

# 为线程定义1个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName,time.ctime(time.time())))

# 创建2个线程
try:
    _thread.start_new_thread(print_time,("Thread-1",2))
    _thread.start_new_thread(print_time,("Thread-2",4))
except:
    print("Error: 无法启动线程")

while 1:
    pass

'''
结果：
Thread-1: Fri Oct 24 15:35:24 2025
Thread-2: Fri Oct 24 15:35:26 2025
Thread-1: Fri Oct 24 15:35:26 2025
Thread-1: Fri Oct 24 15:35:28 2025
Thread-2: Fri Oct 24 15:35:30 2025
Thread-1: Fri Oct 24 15:35:30 2025
Thread-1: Fri Oct 24 15:35:32 2025
Thread-2: Fri Oct 24 15:35:34 2025
Thread-2: Fri Oct 24 15:35:38 2025
Thread-2: Fri Oct 24 15:35:42 2025
'''