# -*- coding: UTF-8 -*-

# filename : test_return_func.py
# description : 返回函数
# author by : peanut
# date : 2025/4/12


"""
    使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：

"""


# 函数中定义函数，最终返回函数
def lazy_sum(*args):
    def do_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return do_sum()


f_obj = lazy_sum(1, 2, 4, 5, 7, 8, 9)


# print(f_obj)
# print(f_obj())


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count1()

print(f1())
print(f2())
print(f3())


# fix:
def count2():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f4, f5, f6 = count2()

print(f1())
print(f2())
print(f3())


def inc1():
    x = 0

    def fn1():
        # 仅读取x的值:
        return x + 1

    return fn1


fs = inc1()
print(fs())  # 1
print(fs())  # 1


def inc2():
    x = 0

    def fn2():
        # 如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错,所以需要使用nonlocal
        nonlocal x
        x = x + 1
        return x

    return fn2


f = inc2()
print(f())  # 1
print(f())  # 2
