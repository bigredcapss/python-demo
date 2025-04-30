# -*- coding: UTF-8 -*-

# filename : test_sort.py
# description : 按字母顺序对列表排序
# author by : peanut
# date : 2025/3/2

"""
    按字母顺序对列表排序，可以使用以下两个方法：
    sort() 方法 -- 即直接修改原始列表，不创建新的排序副本，该方法会改变原列表的顺序，不返回新的排序列表。
    sorted() 函数 -- 创建一个新的已排序列表，不修改原始列表，该函数返回一个新的已排序列表，原列表保持不变。

    无论你选择哪种方法，都可以按字母顺序对列表进行排序。
    如果你希望按字母顺序的反向顺序排序（降序），可以在 sort() 方法或 sorted() 函数中传递 reverse=True 参数。
"""

# sort
my_list1 = ["apple", "banana", "cherry", "date"]
my_list1.sort()  # 按字母顺序排序
print(my_list1)

my_list2 = ["apple", "banana", "cherry", "date"]
my_list2.sort(reverse=True)  # 按字母顺序降序排序
print(my_list2)

# sorted
my_list3 = ["apple", "banana", "cherry", "date"]
sorted_list1 = sorted(my_list3)  # 创建一个新的已排序列表
print(sorted_list1)

my_list2 = ["apple", "banana", "cherry", "date"]
sorted_list2 = sorted(my_list2, reverse=True)  # 创建一个新的已排序列表，按字母顺序降序排序
print(sorted_list2)
