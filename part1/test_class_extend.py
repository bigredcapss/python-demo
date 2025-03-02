# -*- coding: UTF-8 -*-

# filename : test_class_extend.py
# description : 使用继承创建一个子类
# author by : peanut
# date : 2025/3/1

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} is speaking"


class Dog(Animal):
    def speak(self):
        return f"{self.name} is barking."


# 创建父类实例
my_animal = Animal("my_animal")
print(my_animal.speak())


# 创建子类实例
my_dog = Dog("my_dog")
print(my_dog.speak())