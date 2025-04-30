# -*- coding: UTF-8 -*-

# filename : test_list_element_multi.py
# description : 计算列表元素之积
# author by : peanut
# date : 2025/3/6

"""
    定义一个数字列表，并计算列表元素之积。
    例如：
    输入 : list1 = [1, 2, 3] 输出 : 6
    计算：1 * 2 * 3
"""


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
