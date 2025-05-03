# -*- coding: UTF-8 -*-

# filename : test_contextlib.py
# description : 使用contextlib简化上下文管理
# author by : peanut
# date : 2025/5/2


"""
    编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，可以使用@contextlib.contextmanager和生成器来简化代码。
    @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了.
    很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
    @contextmanager让我们通过编写generator来简化上下文管理
"""


from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

    