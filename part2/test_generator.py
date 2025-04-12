# -*- coding: UTF-8 -*-

# filename : test_generator.py
# description : 生成器
# author by : peanut
# date : 2025/4/12


"""
    如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
    这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

    定义generator的另一种方法。如果一个函数定义中包含yield关键字，
    那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator

    最难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
"""

# generator
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"


f = fib(10)
print("fib(10):", f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


"""
    请务必注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
"""
print(next(odd()))

"""
    创建一个generator对象，然后不断对这一个generator对象调用next()
"""
g = odd()
next(g)



