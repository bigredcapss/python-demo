# -*- coding: UTF-8 -*-

# filename : test_reraise.py
# description : 抛出错误
# author by : peanut
# date : 2025/4/12


"""
    在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
    其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
    所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，
    如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
"""


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value: %s" % s)
    return 10 / n


def bar():
    try:
        foo("0")
    except ValueError as e:
        print("ValueError!")
        raise


bar()