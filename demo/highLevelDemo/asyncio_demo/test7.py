#!/usr/bin/python3

# 2. 并发执行任务
import asyncio

async def fetch(url):
    print(f"fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("url1.com"),
        fetch("url2.com")
    )
    print(results)

asyncio.run(main())

'''
输出：
fetching url1.com
fetching url2.com
['Data from url1.com', 'Data from url2.com']
'''