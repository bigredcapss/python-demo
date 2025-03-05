# -*- coding: UTF-8 -*-

# filename : test_swap_head_tail.py
# description : 将列表中的头尾两个元素对调
# author by : peanut
# date : 2025/3/5



"""
    定义一个列表，并将列表中的头尾两个元素对调。
    例如
    对调前 : [1, 2, 3]
    对调后 : [3, 2, 1]

"""


# 方法1
def swapList1(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


newList = [1, 2, 3]

print(swapList1(newList))


# 方法2
def swapList2(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


newList = [1, 2, 3]
print(swapList2(newList))


# 方法3
def swapList3(list):
    get = list[-1], list[0]

    list[0], list[-1] = get

    return list


newList = [1, 2, 3]
print(swapList3(newList))