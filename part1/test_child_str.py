# -*- coding: UTF-8 -*-

# filename : test_child_str.py
# description : 判断字符串是否存在子字符串
# author by : peanut
# date : 2025/3/7


"""
    find函数用于查找子字符串
"""


def check(parent_str, child_str):
    if parent_str.find(child_str) == -1:
        print("不存在！")
    else:
        print("存在！")


par_str = "www.runoob.com"
sub_str = "runoob"
check(par_str, sub_str)
