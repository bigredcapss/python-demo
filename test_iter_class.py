# -*- coding: UTF-8 -*-

# filename : test_iter_class.py
# description : 定义一个迭代器类
# author by : peanut
# date : 2025/3/1


"""
    在 Python 中，迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
    迭代器只能往前不会后退。要创建一个迭代器类，我们需要实现 __iter__() 和 __next__() 方法。
"""


# 定义一个迭代器类
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


# 使用迭代器
my_iter = MyIterator(1, 5)
for num in my_iter:
    print(num)



