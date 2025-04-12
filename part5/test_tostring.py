# -*- coding: UTF-8 -*-

# filename : test_tostring.py
# description : 使用魔术方法 __str__ 来自定义对象的打印输出
# author by : peanut
# date : 2025/3/2


"""
    在 Python 中，魔术方法 __str__ 用于定义对象的字符串表示形式。
    当你使用 print() 函数打印对象时，或者使用 str() 函数将对象转换为字符串时，Python 会自动调用这个方法来获取对象的字符串表示。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# 创建一个 Person 对象
person = Person("Alice", 30)


# 打印对象
print(person)

