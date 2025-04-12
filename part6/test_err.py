# -*- coding: UTF-8 -*-

# filename : test_err.py
# description : 异常调用栈
# author by : peanut
# date : 2025/4/12


"""
    调用栈：如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
"""


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar("0")


main()