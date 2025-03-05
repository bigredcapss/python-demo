# -*- coding: UTF-8 -*-

# filename : test_swap_element.py
# description : 将列表中的指定位置的两个元素对调
# author by : peanut
# date : 2025/3/5


"""
    定义一个列表，并将列表中的指定位置的两个元素对调。
    例如，对调第一个和第三个元素：
    对调前 : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
    对调后 : [19, 65, 23, 90]
"""


# 方法1
def swapPositions1(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions1(List, pos1 - 1, pos2 - 1))


# 方法2
def swapPositions2(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions2(List, pos1 - 1, pos2 - 1))


# 方法3
def swapPositions3(list, pos1, pos2):
    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list


List = [23, 65, 19, 90]

pos1, pos2 = 1, 3
print(swapPositions3(List, pos1 - 1, pos2 - 1))
