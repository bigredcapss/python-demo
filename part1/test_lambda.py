# -*- coding: UTF-8 -*-

# filename : test_lambda.py
# description : 使用 lambda 表达式进行列表排序
# author by : peanut
# date : 2025/3/2


"""
    在 Python 中，lambda 表达式是一种创建匿名函数的方式，通常用于需要一个简单函数但不想正式定义一个函数的场合。
    使用 lambda 表达式可以方便地对列表进行排序，尤其是在需要根据某个特定的条件或属性进行排序时。
    语法：lambda arguments: expression
    arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
    expression 是一个表达式，用于计算并返回函数的结果。
"""


def people_sort():
    # 定义一个包含元组的列表，每个元组包含姓名和年龄
    people = [('Alice', 25), ('Bob', 20), ('Charlie', 30), ('David', 22)]

    # 使用 lambda 表达式进行列表排序
    sorted_numbers = sorted(people, key=lambda x: x[1])

    # 打印排序后的结果
    print(sorted_numbers)


# 调用函数
people_sort()