# -*- coding: UTF-8 -*-

# filename : test_class_method.py
# description : 使用 @classmethod 定义一个类方法
# author by : peanut
# date : 2025/3/1

"""
    在 Python 中，@classmethod 是一个装饰器，用于定义类方法。
    类方法是绑定到类而不是实例的方法，可以通过类本身或类的实例来调用。类方法的第一个参数通常是 cls，它代表类本身。
"""

class MyClass:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_instance(cls, name):
        return cls(name)

    def say_hello(self):
        print(f"Hello, {self.name}!")


# 使用类方法创建实例
my_instance = MyClass.create_instance("Alice")

# 调用实例方法
my_instance.say_hello()




