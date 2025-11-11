#!/usr/bin/python3

'''

asyncio 的基本用法
1. 运行协程
要运行一个协程，你可以使用 asyncio.run() 函数。它会创建一个事件循环，并运行指定的协程。
'''
import asyncio
from datetime import datetime

async def main():
    print(f"{datetime.now():%F %T} Start")
    await asyncio.sleep(3)
    print(f"{datetime.now():%F %T} End")

asyncio.run(main())

'''
输出：
2025-11-07 11:34:39 Start
2025-11-07 11:34:42 End

f"{datetime.now():%F %T}" 是一条f-string 格式指令，把 datetime.now() 直接格式化成**“年-月-日 时:分:秒”**的字符串。
表格
复制
格式符	含义	示例输出
%F	等价于 %Y-%m-%d（ISO 日期）	2025-06-25
%T	等价于 %H:%M:%S（24 时时间）	14:08:17
'''