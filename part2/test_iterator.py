# -*- coding: UTF-8 -*-

# filename : test_iterator.py
# description : 迭代器
# author by : peanut
# date : 2025/4/12

from collections.abc import Iterable, Iterator


"""
    凡是可作用于for循环的对象都是Iterable类型；
    凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
"""


def g():
    yield 1
    yield 2
    yield 3


print("Iterable? [1, 2, 3]:", isinstance([1, 2, 3], Iterable))
print("Iterable? 'abc':", isinstance("abc", Iterable))
print("Iterable? 123:", isinstance(123, Iterable))
print("Iterable? g():", isinstance(g(), Iterable))

print("Iterator? [1, 2, 3]:", isinstance([1, 2, 3], Iterator))
print("Iterator? iter([1, 2, 3]):", isinstance(iter([1, 2, 3]), Iterator))
print("Iterator? 'abc':", isinstance("abc", Iterator))
print("Iterator? 123:", isinstance(123, Iterator))
print("Iterator? g():", isinstance(g(), Iterator))