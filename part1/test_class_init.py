# -*- coding: UTF-8 -*-

# filename : test_class_init.py
# description : 创建一个类并实例化它
# author by : peanut
# date : 2025/3/1


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking!"


# 实例化类
my_dog = Dog("Max", 3)

# 访问属性和调用方法
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())

