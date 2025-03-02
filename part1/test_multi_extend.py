# -*- coding: UTF-8 -*-

# filename : test_multi_extend.py
# description : 创建一个多继承的类
# author by : peanut
# date : 2025/3/1


"""
    在 Python 中，多继承是指一个类可以继承多个父类。通过多继承，子类可以继承多个父类的属性和方法。
"""


class Parent1:
    def method1(self):
        print("Parent1 method1")


class Parent2:
    def method2(self):
        print("Parent2 method2")


class Child(Parent1, Parent2):
    def method3(self):
        print("Child method3")


# 创建 Child 类的实例
child = Child()

# 调用继承自 Parent1 的方法
child.method1()

# 调用继承自 Parent2 的方法
child.method2()

# 调用 Child 类自己的方法
child.method3()