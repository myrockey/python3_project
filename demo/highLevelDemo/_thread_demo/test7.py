#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue
import threading
import time
import random                     # 仅用于模拟耗时

# ---------------------------- 线程池规模 & 任务源 ----------------------------
WORKER_THREADS = 3
TASKS = ["one", "two", "three", "four", "five"]

# ---------------------------- 工作线程 ----------------------------
def worker(worker_id: int, q: queue.Queue):
    """消费任务直到收到 None（优雅退出信号）。"""
    while True:
        item = q.get()                      # 阻塞式取任务
        if item is None:                    # None → 退出信号
            q.task_done()                   # 把退出信号也标记完成
            break

        # 模拟业务耗时（0~2 秒）
        time.sleep(random.uniform(0, 2))
        print(f"[Worker-{worker_id}] 处理 → {item}")
        q.task_done()                       # 告诉队列“我干完了”
    print(f"[Worker-{worker_id}] 正常退出")

# ---------------------------- 主线程 ----------------------------
def main():
    q = queue.Queue()                       # 线程安全队列，自带阻塞

    # 1. 启动工作线程
    threads = []
    for i in range(WORKER_THREADS):
        t = threading.Thread(target=worker, args=(i, q), daemon=False)
        t.start()
        threads.append(t)

    # 2. 投放任务
    for task in TASKS:
        q.put(task)

    # 3. 等待所有任务完成（无忙等）
    q.join()                                # 阻塞到 queue 空且 task_done 计数归零

    # 4. 发送退出信号（None 个数 = 工作线程个数）
    for _ in range(WORKER_THREADS):
        q.put(None)

    # 5. 等待线程真正结束
    for t in threads:
        t.join()

    print("【主线程】所有工作完成，安全退出。")

if __name__ == '__main__':
    main()


'''
结果:
[Worker-0] 处理 → one
[Worker-2] 处理 → three
[Worker-0] 处理 → four
[Worker-1] 处理 → two
[Worker-2] 处理 → five
[Worker-0] 正常退出
[Worker-2] 正常退出
[Worker-1] 正常退出
【主线程】所有工作完成，安全退出。
'''