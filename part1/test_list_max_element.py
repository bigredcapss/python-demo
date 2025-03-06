# -*- coding: UTF-8 -*-

# filename : test_list_max_element.py
# description : 查找列表中最大元素
# author by : peanut
# date : 2025/3/6

"""
    定义一个数字列表，并查找列表中的最小元素。
    例如
    输入 : list1 = [10, 20, 4]
    输出 : 4
"""


# demo1
list1 = [10, 20, 4]

print(max(list1))


# demo2
list1 = [10, 20, 4]

list1.sort()

print("最大元素为:", list1[-1])
