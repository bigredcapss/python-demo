# -*- coding: UTF-8 -*-

# filename : test_with.py
# description : 使用with
# author by : peanut
# date : 2025/5/2


"""
    写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：

    with open('/path/to/file', 'r') as f:
        f.read()

    并不是只有open()函数返回的资源才需要关闭，实际上任何实现了__enter__()和__exit__()方法的对象，都可以用于with语句。
"""


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def query(self):
        print('Query info about %s...' % self.name)



with Query('Bob') as q:
    q.query()







