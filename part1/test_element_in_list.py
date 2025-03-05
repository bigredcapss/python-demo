# -*- coding: UTF-8 -*-

# filename : test_element_in_list.py
# description : 判断元素是否在列表中存在
# author by : peanut
# date : 2025/3/5


"""
    定义一个列表，并判断元素是否在列表中。
"""

test_list = [1, 6, 3, 5, 3, 4]

print("查看 4 是否在列表中 ( 使用循环 ) : ")

for i in test_list:
    if i == 4:
        print("存在")

print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ")

if 4 in test_list:
    print("存在")

# 初始化列表
test_list_set = [1, 6, 3, 5, 3, 4]
test_list_bisect = [1, 6, 3, 5, 3, 4]

print("查看 4 是否在列表中 ( 使用 set() + in) : ")

test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("存在")

print("查看 4 是否在列表中 ( 使用 count()) : ")

if test_list_bisect.count(4) > 0:
    print("存在")