#!/usr/bin/python3

# 1. 基本协程示例
import asyncio

async def hello():
    print("hello")
    await asyncio.sleep(3)
    print("world")

asyncio.run(hello()) # Python3.7+