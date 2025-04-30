# -*- coding: UTF-8 -*-

# filename : test_copy_list.py
# description : 复制列表
# author by : peanut
# date : 2025/3/6


"""
    定义一个列表，并将该列表元素复制到另外一个列表上。
"""


# demo1
def clone_runoff1(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoff1(li1)
print("原始列表:", li1)
print("复制后列表:", li2)


# demo2
#  使用 extend() 方法
def clone_runoff2(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoff2(li1)
print("原始列表:", li1)
print("复制后列表:", li2)


# demo3
# 使用list方法
def clone_runoff3(li1):
    li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoff3(li1)
print("原始列表:", li1)
print("复制后列表:", li2)



