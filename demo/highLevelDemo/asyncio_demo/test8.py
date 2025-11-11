#!/usr/bin/python3

# 3. 使用异步队列
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"producer {i}")
        await asyncio.sleep(0.1)
    await queue.put(None)          # 哨兵

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:           # 收到哨兵，退出
            queue.task_done()
            break
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producerTask = asyncio.create_task(producer(queue))
    consumerTask = asyncio.create_task(consumer(queue))
    await producerTask          # 等生产完
    await queue.join()  # 等所有 task_done()
    consumerTask.cancel()       # 主动取消无限循环
    print("all done")

asyncio.run(main())

'''
输出：
producer 0
Consumed 0
producer 1
Consumed 1
producer 2
Consumed 2
producer 3
Consumed 3
producer 4
Consumed 4
all done
'''