# -*- coding: UTF-8 -*-

# filename : test_iter.py
# description : 迭代操作与迭代器
# author by : peanut
# date : 2025/4/12

from collections.abc import Iterable

"""
    list
    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
"""



# 迭代器函数
def g():
    yield 1
    yield 2
    yield 3


print("Iterable? [1, 2, 3]:", isinstance([1, 2, 3], Iterable))
print("Iterable? 'abc':", isinstance("abc", Iterable))
print("Iterable? 123:", isinstance(123, Iterable))
print("Iterable? g():", isinstance(g(), Iterable))

# iter list:
print("for x in [1, 2, 3, 4, 5]:")
for x in [1, 2, 3, 4, 5]:
    print(x)

print("for x in iter([1, 2, 3, 4, 5]):")
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print("next():")
# 把列表通过iter函数变成迭代器（Iterator）
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {"a": 1, "b": 2, "c": 3}

# iter each key:
print("iter key:", d)
for k in d.keys():
    print("key:", k)

# iter each value:
print("iter value:", d)
for v in d.values():
    print("value:", v)

# iter both key and value:
print("iter item:", d)
for k, v in d.items():
    print("item:", k, v)

# iter list with index:
print("iter enumerate(['A', 'B', 'C']")
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)

# iter complex list:
print("iter [(1, 1), (2, 4), (3, 9)]:")
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)