#!/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        print('开始线程:'+self.name)
        print_time(self.name,self.delay,5)
        print('退出线程:'+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(1,"Thread-2",2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")

'''
结果：
开始线程:Thread-1
开始线程:Thread-2
Thread-1: Fri Oct 24 15:48:43 2025
Thread-2: Fri Oct 24 15:48:44 2025
Thread-1: Fri Oct 24 15:48:44 2025
Thread-1: Fri Oct 24 15:48:45 2025
Thread-2: Fri Oct 24 15:48:46 2025
Thread-1: Fri Oct 24 15:48:46 2025
Thread-1: Fri Oct 24 15:48:47 2025
退出线程:Thread-1
Thread-2: Fri Oct 24 15:48:48 2025
Thread-2: Fri Oct 24 15:48:50 2025
Thread-2: Fri Oct 24 15:48:52 2025
退出线程:Thread-2
退出主线程
'''