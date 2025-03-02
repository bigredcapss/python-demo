# -*- coding: UTF-8 -*-

# filename : test_repr.py
# description : 实现一个类，通过 __repr__ 法返回自定义对象的描述
# author by : peanut
# date : 2025/3/2


"""
    创建一个简单的类 Person，并通过 __repr__ 方法返回该对象的自定义描述。
    __repr__ 方法通常用于生成一个对象的"官方"字符串表示，通常用于调试和日志记录
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# 创建一个 Person 对象
person = Person("Alice", 30)

# 打印对象的描述
print(person)



