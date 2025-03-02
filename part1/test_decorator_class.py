# -*- coding: UTF-8 -*-

# filename : test_decorator_class.py
# description : 实现一个类装饰器
# author by : peanut
# date : 2025/3/2


"""
    类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数
"""


class DecoratorClass:
    def __init__(self, func):
        self.func = func
        print(f"DecoratorClass initialized with function: {func.__name__}")

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result


"""
   @DecoratorClass 是一个语法糖，等价于 my_function = DecoratorClass(my_function)
"""


@DecoratorClass
def my_function():
    print("Inside my_function")


# 调用 my_function
my_function()


