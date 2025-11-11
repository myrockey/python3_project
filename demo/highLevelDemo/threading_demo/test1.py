#!/usr/bin/python3

import threading

# 可以通过继承 threading.Thread 类或直接使用 threading.Thread 构造函数来创建线程。

# 继承 threading.Thread
class MyThread(threading.Thread):
    def run(self):
        print('线程开始执行')
        # 执行的代码
        print('线程执行结束')

def test1():
    thread = MyThread()
    thread.start()
    thread.join()
    print('主线程结束')

# test1()

# 直接使用 threading.Thread
def my_function():
    print('线程开始执行')
    # 执行的代码
    print('线程执行结束')

def test2():
    thread = threading.Thread(target=my_function)
    thread.start()
    thread.join()
    print('主线程结束')

# test2()

'''
2. 线程同步
在多线程编程中，多个线程可能会同时访问共享资源，这可能导致数据不一致的问题。为了避免这种情况，可以使用线程同步机制，如锁（Lock）。
'''
def task():
    print('线程开始执行')
    # 执行的代码
    print('线程执行结束')

def test3():
    # 创建线程实例
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    # 启动线程
    thread1.start()
    thread2.start()
    # 等待线程执行完毕
    thread1.join()
    thread2.join()
    print('主线程结束')

# test3()
"""
输出：
线程开始执行
线程开始执行
线程执行结束
线程执行结束
主线程结束

这段代码没有任何问题，是“多线程并发 + 同步等待”的标准模板：
两个线程并发执行 task()
start() 立即返回，两个线程在后台并行跑
join() 保证主线程最后才打印 '主线程结束'
运行效果（可能乱序，但一定等俩线程结束）

小技巧 / 注意点
顺序不确定
两次 "线程开始执行" 谁先谁后由操作系统调度，别写依赖顺序的逻辑。
共享数据要加锁
如果 task() 里会修改全局变量，用 threading.Lock() 保护：
Python
复制
lock = threading.Lock()
def task():
    with lock:
        # 修改共享数据
"""