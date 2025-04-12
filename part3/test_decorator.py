# -*- coding: UTF-8 -*-

# filename : test_decorator.py
# description : 装饰器
# author by : peanut
# date : 2025/4/12


import functools

"""
    函数对象有一个__name__属性，可以拿到函数的名字
    在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
    本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

"""

"""
    观察下面的log1，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
    调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
"""


def log1(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log1
def now1():
    print('2025-4-12')


print(now1())

"""
    剖析下面的语句，首先执行log2('execute')，返回的是decorator函数，再调用返回的decorator函数，参数是now函数，返回值最终是wrapper函数。
    以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
    但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
    
    因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
    否则，有些依赖函数签名的代码执行就会出错。
    不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
    所以，一个完整的decorator的写法如下
    
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    针对带参数的decorator如下
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
"""


def log2(text):
    def decorator(func):

        # @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('execute')
def now2():
    print('2025-04-09')


f = now2
print(f())

print(now2.__name__)
