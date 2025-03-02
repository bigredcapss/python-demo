# -*- coding: UTF-8 -*-

# filename : test_stack.py
# description : 使用Python实现一个简单的栈（Stack）类
# author by : peanut
# date : 2025/3/2


"""
    栈（Stack）是一种遵循后进先出（LIFO）原则的数据结构。我们可以使用 Python 的列表来实现一个简单的栈类。这个类将包含以下几个基本操作：
    push(item)：将元素 item 压入栈顶。
    pop()：移除并返回栈顶的元素。
    peek()：返回栈顶的元素但不移除它。
    is_empty()：检查栈是否为空。
    size()：返回栈中元素的数量。
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


# 示例使用
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # 输出: 3
print(stack.pop())  # 输出: 3
print(stack.size())  # 输出: 2
print(stack.is_empty())  # 输出: False
stack.pop()
stack.pop()
print(stack.is_empty())  # 输出: True
