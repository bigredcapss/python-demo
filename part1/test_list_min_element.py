# -*- coding: UTF-8 -*-

# filename : test_list_min_element.py
# description : 查找列表中最小元素
# author by : peanut
# date : 2025/3/6

"""
    定义一个数字列表，并查找列表中的最小元素。
    例如
    输入 : list1 = [10, 20, 4]
    输出 : 4

    知识点：
    list[start:end:step] 是Python的切片操作标准格式：
    - **start**: 起始索引（包含）
    - **end**: 结束索引（不包含）
    - **step**: 步长（默认1，可为负数）
"""


# demo1
list1 = [10, 20, 4, 45, 99]

list1.sort()

# print(*[4]) 等价于 print(4)（将列表解包为独立参数）
# [:1] 是切片操作，表示取列表前 1 个元素
print("最小元素为:", *list1[:1])


# demo2
list1 = [10, 20, 1, 45, 99]

print("最小元素为:", min(list1))