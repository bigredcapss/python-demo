# -*- coding: UTF-8 -*-

# filename : test_raise.py
# description : 抛出错误
# author by : peanut
# date : 2025/4/12


"""
    因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
    Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
    如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
"""


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
