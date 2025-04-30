# -*- coding: UTF-8 -*-

# filename : test_higher_order_function.py
# description : 高阶函数
# author by : peanut
# date : 2025/4/12


from functools import reduce
from operator import itemgetter

"""
    一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
"""


def add(f, *args):
    s = [f(arg) for arg in args]
    return sum(s)


print(add(abs, 10, -20, 30, -40))

"""
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
"""


def f(x):
    return x * x


# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

"""
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""

CHAR_TO_INT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int("0"))
print(str2int("12300"))
print(str2int("0012345"))

CHAR_TO_FLOAT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": -1}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float("0"))
print(str2float("123.456"))
print(str2float("123.45600"))
print(str2float("0.1234"))
print(str2float(".1234"))
print(str2float("120.0034"))


"""
    filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
    然后根据返回值是True还是False决定保留还是丢弃该元素。
    
    filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
"""


def is_odd(n):
    return n % 2 == 1


L = range(100)

print(list(filter(is_odd, L)))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["A", "", "B", None, "C", "  "])))


"""
    sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
"""


li = ["bob", "about", "Zoo", "Credit"]

print(sorted(L))
print(sorted(L, key=str.lower))

students = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))