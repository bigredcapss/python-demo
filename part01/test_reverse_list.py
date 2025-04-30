# -*- coding: UTF-8 -*-

# filename : test_reverse_list.py
# description : 翻转列表
# author by : peanut
# date : 2025/3/5


"""
    定义一个列表，并将它翻转。
    例如：
    翻转前 : list = [10, 11, 12, 13, 14, 15]
    翻转后 : [15, 14, 13, 12, 11, 10]
"""


# 方法1
def reverse1(lst):
    return [ele for ele in reversed(lst)]


lst = [10, 11, 12, 13, 14, 15]
print(reverse1(lst))


# 方法2
def reverse2(lst):
    lst.reverse()
    return lst


lst = [10, 11, 12, 13, 14, 15]
print(reverse2(lst))


# 方法3
def reverse3(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(reverse3(lst))



