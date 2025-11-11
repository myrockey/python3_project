#!/usr/bin/python3

'''
2. 并发执行多个任务
你可以使用 asyncio.gather() 函数并发执行多个协程，并等待它们全部完成。
'''
import asyncio

async def task1():
    print("Task1 started")
    await asyncio.sleep(1)
    print("Task1 finished")

async def task2():
    print("Task2 started")
    await asyncio.sleep(1)
    print("Task2 finished")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())

'''
输出：
Task1 started
Task2 started
Task1 finished
Task2 finished
'''