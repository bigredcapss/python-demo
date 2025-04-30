# -*- coding: UTF-8 -*-

# filename : test_queue.py
# description : 使用python实现一个简单的队列（Queue）
# author by : peanut
# date : 2025/3/2

"""
    队列（Queue）是一种先进先出（FIFO）的数据结构。我们可以使用 Python 的列表来实现一个简单的队列类。这个类将包含以下几个基本操作：
    enqueue(item)：将元素添加到队列的末尾。
    dequeue()：移除并返回队列的第一个元素。
    is_empty()：检查队列是否为空。
    size()：返回队列中元素的数量
"""

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise None
        return self.queue.pop(0)


# 示例使用
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 输出: 1
print(q.size())     # 输出: 2
print(q.is_empty()) # 输出: False

