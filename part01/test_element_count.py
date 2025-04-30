# -*- coding: UTF-8 -*-

# filename : test_element_count.py
# description : 计算元素在列表中出现的次数
# author by : peanut
# date : 2025/3/6


"""
定义一个列表，并计算某个元素在列表中出现的次数。
例如：
输入 : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
       x = 10
输出 : 3
"""


# demo1
def count_x1(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(count_x1(lst, x))


# demo2
# 使用count方法
def count_x2(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(count_x2(lst, x))





