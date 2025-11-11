#!/usr/bin/python3
import queue, threading,time

# 错误示例
def test():
    q = queue.Queue(maxsize=3)  # 容量为3的队列

    def producer():
        for i in range(5):
            q.put(f"Task-{i}")
            print(f"Produced: Task-{i}")
            time.sleep(3)

    def consumer():
        while True:
            item = q.get()
            print(f"Consumed: {item}")
            q.task_done()

    threading.Thread(target=producer, daemon=True).start()
    threading.Thread(target=consumer, daemon=True).start()
    q.join()  # 等待所有任务完成

# test()
'''
结果：
Produced: Task-0
Consumed: Task-0

由于消费者快，生产者慢，导致q.join() == 0很快就退出了，生产者还没完全推送完成，所以这种写法是错误示例

'''

# 优先级任务处理
def PriorityQueue_task():
    pq = queue.PriorityQueue()
    pq.put((3,"Can"))
    pq.put((1,"hello"))
    pq.put((2,"world"))

    while not pq.empty():
        # print(pq.get()) # (1,'hello')
        print(pq.get()[1]) # hello

# PriorityQueue_task()

'''
输出：
hello
world
Can

'''

# 非阻塞式消费者获取消息
def test2():
    q = queue.Queue()
    def producer():
        for i in range(5):
            q.put(i)
            print(f"Produced: {i}")
            time.sleep(0.01)
    
    # 非阻塞式消费
    def consumer():
        while True:
            try:
                item = q.get_nowait()  # 等价于 q.get(block=False) 当没获取到消息raise 抛出queue.Empty异常
                if(item == 'None'):
                    print('consumer None，退出')
                    break
                q.task_done()
                print(f'consumer {item}')
            except queue.Empty:
                print("队列为空")
                # time.sleep(0.1)

    producer_thread = threading.Thread(target=producer,daemon=True)
    consumer_thread = threading.Thread(target=consumer,daemon=True)

    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    q.join()
    q.put('None')
    print('主线程推送None，准备退出')
    consumer_thread.join()
    print('主线程正常退出')

test2()