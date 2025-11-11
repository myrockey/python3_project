#!/usr/bin/python3

import queue,threading,time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire() # 获取锁
        if not workQueue.empty():
            data = q.get()
            queueLock.release() # 释放锁
            print("%s processing %s %s" % (threadName,data,time.ctime(time.time())))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["one","two","three","four","five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty(): #在这里循环等到队列为空
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

'''
结果：
开启线程：Thread-1
开启线程：Thread-2
开启线程：Thread-3
Thread-3 processing one
Thread-1 processing two
Thread-2 processing three
Thread-3 processing four
Thread-1 processing five
退出线程：Thread-2
退出线程：Thread-3
退出线程：Thread-1
退出主线程
'''