# -*- coding: UTF-8 -*-

# filename : test_assert.py
# description : 断言
# author by : peanut
# date : 2025/4/12


def foo(s):
    n = int(s)
    assert n != 0, "n is zero!"
    return 10 / n


def main():
    foo("0")


main()
