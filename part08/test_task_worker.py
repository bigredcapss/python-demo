# -*- coding: UTF-8 -*-

# filename : test_task_worker.py
# description : 分布式进程的使用
# author by : peanut
# date : 2025/4/30


"""
    Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
    注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，
    就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
    在另一台机器上启动任务进程（本机上启动也可以）
    任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。
    现在，可以试试分布式进程的工作效果了。先启动task_master.py服务进程：

"""



import time, sys, queue
from multiprocessing.managers import BaseManager

def run_worker():
    # 创建类似的QueueManager:
    class QueueManager(BaseManager):
        pass

    # 注册Queue:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    m.connect()

    # 获取Queue对象:
    task = m.get_task_queue()
    result = m.get_result_queue()

    # 处理任务:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')
    print('worker exit.')

if __name__ == '__main__':
    run_worker()
