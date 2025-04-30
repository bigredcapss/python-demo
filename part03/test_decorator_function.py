# -*- coding: UTF-8 -*-

# filename : test_decorator_function.py
# description : 实现一个装饰器函数
# author by : peanut
# date : 2025/3/2


"""
    装饰器是 Python 中一种强大的工具，它允许你在不修改原函数代码的情况下，增加额外的功能。
    装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数。
"""


def my_decorator(original_func):
    """
        装饰器函数，接受一个函数作为参数，并返回一个新的函数。
    """

    def wrapper():
        """
            新的函数，在原函数执行前和后分别执行一些操作。
        """

        print("Before function execution")
        original_func()
        print("After function execution")

    return wrapper


"""
    @my_decorator 是 Python 的装饰器语法糖，它等价于 say_hello = my_decorator(say_hello)
"""


@my_decorator
def original():
    print("This is the original function")


"""
    repeat 函数是一个带参数的装饰器，它接受一个整数参数 n，然后返回一个装饰器函数。
    该装饰器函数内部定义了 wrapper 函数，在调用原始函数之前重复执行 n 次。
    因此，greet 函数在被 @repeat(3) 装饰后，会打印三次问候语。
"""


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


# 调用greet函数
greet("Alice")


# 调用func函数
original()