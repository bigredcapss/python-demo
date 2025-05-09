# -*- coding: UTF-8 -*-

# filename : test_defi_function.py
# description : 定义函数
# author by : peanut
# date : 2025/4/12


import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
my_abs('123')

