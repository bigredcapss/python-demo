# -*- coding: UTF-8 -*-

# filename : test_child_process.py
# description : 通过Pool创建多个子进程
# author by : peanut
# date : 2025/4/27

"""
    如果要启动大量的子进程，可以用进程池的方式批量创建子进程;
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    请注意输出的结果，task 0，1，2，3,4,5,6,7,8,9是立刻执行的，而task 10要等待前面某个task完成后才执行，
    这是因为Pool的默认大小在我的电脑上是10，因此，最多同时执行10个进程。这是Pool有意设计的限制，并不是操作系统的限制,如果改成：
    p = Pool(5)
    就可以同时跑5个进程。
    由于Pool的默认大小是CPU的核数，如果你拥有16核CPU，你要提交至少33个子进程才能看到上面的等待效果。

    apply_async 方法:apply_async 是 Pool 类的一个方法，用于异步地将一个函数提交到进程池中执行。
    与 apply 方法不同，apply_async 不会阻塞主进程，而是立即返回一个 AsyncResult 对象，该对象可以用于检查任务的状态或获取任务的结果
"""

import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(10)
    for i in range(11):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
