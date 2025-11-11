#!/usr/bin/python3

'''
3. 超时控制
你可以使用 asyncio.wait_for() 函数为协程设置超时时间。如果协程在指定时间内未完成，将引发 asyncio.TimeoutError 异常。
'''
import asyncio

async def long_task():
    await asyncio.sleep(3)
    print("Task finished")

async def main():
    try:
        await asyncio.wait_for(long_task(),timeout=2)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())

'''
输出：
Task timed out
'''