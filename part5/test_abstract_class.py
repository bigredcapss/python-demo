# -*- coding: UTF-8 -*-

# filename : test_abstract_class.py
# description : 使用抽象类定义接口
# author by : peanut
# date : 2025/3/1

"""
    在 Python 中，抽象类是一种特殊的类，它不能被实例化，只能被继承。
    抽象类通常用于定义接口，即一组方法的声明，而不提供具体的实现。子类必须实现这些方法才能被实例化。
    Python 提供了 abc 模块来创建抽象类。我们可以使用 ABC 类和 abstractmethod 装饰器来定义抽象方法。
"""

from abc import ABC, abstractmethod


# 通过继承ABC定义抽象类Animal
# 定义了两个抽象方法 make_sound 和 move，这些方法没有具体的实现
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("wo wo")

    def move(self):
        print("Running on four legs")


class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flying in the sky"


# 实例化子类
dog = Dog()
bird = Bird()

print(dog.make_sound())  # 输出: Woof!
print(dog.move())        # 输出: Running on four legs

print(bird.make_sound()) # 输出: Chirp!
print(bird.move())       # 输出: Flying in the sky





