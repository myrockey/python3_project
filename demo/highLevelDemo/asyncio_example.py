"""
Python asyncio 模块
asyncio 是 Python 标准库中的一个模块，用于编写异步 I/O 操作的代码。

asyncio 提供了一种高效的方式来处理并发任务，特别适用于 I/O 密集型操作，如网络请求、文件读写等。

通过使用 asyncio，你可以在单线程中同时处理多个任务，而无需使用多线程或多进程。

为什么需要 asyncio？
在传统的同步编程中，当一个任务需要等待 I/O 操作（如网络请求）完成时，程序会阻塞，直到操作完成。这会导致程序的效率低下，尤其是在需要处理大量 I/O 操作时。

asyncio 通过引入异步编程模型，允许程序在等待 I/O 操作时继续执行其他任务，从而提高了程序的并发性和效率。

asyncio 的核心概念
1. 协程（Coroutine）
协程是 asyncio 的核心概念之一。它是一个特殊的函数，可以在执行过程中暂停，并在稍后恢复执行。协程通过 async def 关键字定义，并通过 await 关键字暂停执行，等待异步操作完成。

实例
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
2. 事件循环（Event Loop）
事件循环是 asyncio 的核心组件，负责调度和执行协程。它不断地检查是否有任务需要执行，并在任务完成后调用相应的回调函数。

实例
async def main():
    await say_hello()

asyncio.run(main())
3. 任务（Task）
任务是对协程的封装，表示一个正在执行或将要执行的协程。你可以通过 asyncio.create_task() 函数创建任务，并将其添加到事件循环中。

实例
async def main():
    task = asyncio.create_task(say_hello())
    await task
4. Future
Future 是一个表示异步操作结果的对象。它通常用于底层 API，表示一个尚未完成的操作。你可以通过 await 关键字等待 Future 完成。

实例
async def main():
    future = asyncio.Future()
    await future
asyncio 的基本用法
1. 运行协程
要运行一个协程，你可以使用 asyncio.run() 函数。它会创建一个事件循环，并运行指定的协程。

实例
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
2. 并发执行多个任务
你可以使用 asyncio.gather() 函数并发执行多个协程，并等待它们全部完成。

实例
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
3. 超时控制
你可以使用 asyncio.wait_for() 函数为协程设置超时时间。如果协程在指定时间内未完成，将引发 asyncio.TimeoutError 异常。

实例
import asyncio

async def long_task():
    await asyncio.sleep(10)
    print("Task finished")

async def main():
    try:
        await asyncio.wait_for(long_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())
asyncio 的应用场景
asyncio 特别适用于以下场景：

网络请求：如 HTTP 请求、WebSocket 通信等。
文件 I/O：如异步读写文件。
数据库操作：如异步访问数据库。
实时数据处理：如实时消息队列处理。
常用类、方法和函数
1. 核心函数
方法/函数	说明	示例
asyncio.run(coro)	运行异步主函数（Python 3.7+）	asyncio.run(main())
asyncio.create_task(coro)	创建任务并加入事件循环	task = asyncio.create_task(fetch_data())
asyncio.gather(*coros)	并发运行多个协程	await asyncio.gather(task1, task2)
asyncio.sleep(delay)	异步等待（非阻塞）	await asyncio.sleep(1)
asyncio.wait(coros)	控制任务完成方式	done, pending = await asyncio.wait([task1, task2])
2. 事件循环（Event Loop）
方法	说明	示例
loop.run_until_complete(future)	运行直到任务完成	loop.run_until_complete(main())
loop.run_forever()	永久运行事件循环	loop.run_forever()
loop.stop()	停止事件循环	loop.stop()
loop.close()	关闭事件循环	loop.close()
loop.call_soon(callback)	安排回调函数立即执行	loop.call_soon(print, "Hello")
loop.call_later(delay, callback)	延迟执行回调	loop.call_later(5, callback)
3. 协程（Coroutine）与任务（Task）
方法/装饰器	说明	示例
@asyncio.coroutine	协程装饰器（旧版，Python 3.4-3.7）	@asyncio.coroutine
def old_coro():
async def	定义协程（Python 3.5+）	async def fetch():
task.cancel()	取消任务	task.cancel()
task.done()	检查任务是否完成	if task.done():
task.result()	获取任务结果（需任务完成）	data = task.result()
4. 同步原语（类似threading）
类	说明	示例
asyncio.Lock()	异步互斥锁	lock = asyncio.Lock()
async with lock:
asyncio.Event()	事件通知	event = asyncio.Event()
await event.wait()
asyncio.Queue()	异步队列	queue = asyncio.Queue()
await queue.put(item)
asyncio.Semaphore()	信号量	sem = asyncio.Semaphore(5)
async with sem:
5. 网络与子进程
方法/类	说明	示例
asyncio.open_connection()	建立TCP连接	reader, writer = await asyncio.open_connection('host', 80)
asyncio.start_server()	创建TCP服务器	server = await asyncio.start_server(handle, '0.0.0.0', 8888)
asyncio.create_subprocess_exec()	创建子进程	proc = await asyncio.create_subprocess_exec('ls')
6. 实用工具
方法	说明	示例
asyncio.current_task()	获取当前任务	task = asyncio.current_task()
asyncio.all_tasks()	获取所有任务	tasks = asyncio.all_tasks()
asyncio.shield(coro)	保护任务不被取消	await asyncio.shield(critical_task)
asyncio.wait_for(coro, timeout)	带超时的等待	try: await asyncio.wait_for(task, 5)
实例
1. 基本协程示例

实例
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())  # Python 3.7+
2. 并发执行任务

实例
async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("url1.com"),
        fetch("url2.com")
    )
    print(results)

asyncio.run(main())
3. 使用异步队列

实例
async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )
注意事项
Python版本：部分功能需Python 3.7+（如asyncio.run()）。

阻塞操作：避免在协程中使用同步阻塞代码（如time.sleep()）。

调试：设置PYTHONASYNCIODEBUG=1环境变量可启用调试模式。

取消任务：被取消的任务会引发CancelledError，需妥善处理。
"""