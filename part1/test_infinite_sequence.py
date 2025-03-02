# -*- coding: UTF-8 -*-

# filename : test_infinite_sequence.py
# description : 使用生成器实现一个无限序列
# author by : peanut
# date : 2025/3/1

"""
    在 Python 中，生成器是一种特殊的迭代器，它允许你按需生成值，而不是一次性生成所有值。
    生成器非常适合用于处理无限序列，因为它们只在需要时生成值，从而节省内存。
"""


def infinite_sequence():
    num = 0
    while True:
        # yield num 使用 yield 关键字返回当前的 num 值，并暂停函数的执行，直到下一次调用 next()
        yield num
        num += 1


# 使用生成器生成无限序列
gen = infinite_sequence()


# 输出前10个值
for i in range(10):
    print(next(gen))