#!/usr/bin/python3

import asyncio

'''
1. 协程（Coroutine）
协程是 asyncio 的核心概念之一。它是一个特殊的函数，可以在执行过程中暂停，并在稍后恢复执行。协程通过 async def 关键字定义，并通过 await 关键字暂停执行，等待异步操作完成。
'''
async def say_hello():
    print("hello")
    await asyncio.sleep(3)
    print("world")

'''
2. 事件循环（Event Loop）
事件循环是 asyncio 的核心组件，负责调度和执行协程。它不断地检查是否有任务需要执行，并在任务完成后调用相应的回调函数。
'''
async def main():
    await say_hello()

# asyncio.run(main())

'''
3. 任务（Task）
任务是对协程的封装，表示一个正在执行或将要执行的协程。你可以通过 asyncio.create_task() 函数创建任务，并将其添加到事件循环中。
'''
async def main2():
    task = asyncio.create_task(say_hello())
    await task

# asyncio.run(main2())

'''
4. Future
Future 是一个表示异步操作结果的对象。它通常用于底层 API，表示一个尚未完成的操作。你可以通过 await 关键字等待 Future 完成。
'''
async def main3():
    future = asyncio.Future()
    await future
