# -*- coding: UTF-8 -*-

# filename : test_static_method.py
# description : 使用 @staticmethod 定义一个静态方法
# author by : peanut
# date : 2025/3/1


"""
    在 Python 中，staticmethod 是一个装饰器，用于定义一个静态方法。
    静态方法不依赖于类的实例，也不依赖于类本身。它们通常用于执行与类相关但不依赖于类或实例状态的操作。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18


person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

print(Person.is_adult(person1.age))  # True
print(Person.is_adult(person2.age))  # False


