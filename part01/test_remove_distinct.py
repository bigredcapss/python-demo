# -*- coding: UTF-8 -*-

# filename : test_remove_distinct.py
# description : 移除列表中重复的元素
# author by : peanut
# date : 2025/3/6

"""
    Python 集合：集合（set）是一个无序的不重复元素序列。
    Python 列表：列表是一种数据项构成的有限序列，即按照一定的线性顺序排列而成的数据项的集合，
    在这种数据结构上进行的基本操作包括对元素的的查找、插入和删除。
"""

# demo1
list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))


# demo2
# 使用辅助集合保持顺序地去重
def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list


# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)  # 输出: [1, 2, 3, 4, 5]


# demo3
# dict.fromkeys() 方法也可以用于去重并保持顺序，因为字典在 Python 3.7 及以上版本中保持插入顺序
# 使用dict.fromkeys()保持顺序地去重
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)  # 输出: [1, 2, 3, 4, 5]


# demo4
# 列表推导式结合条件判断也可以实现去重功能。
def remove_duplicates(lst):
    unique_list = []
    [unique_list.append(item) for item in lst if item not in unique_list]
    return unique_list


# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)  # 输出: [1, 2, 3, 4, 5]


# demo5
# ^ 得到两个列表的对称差（排除两个集合的重叠元素）
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))
