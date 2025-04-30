# -*- coding: UTF-8 -*-

# filename : test_str_lenth.py
# description : 判断字符串长度
# author by : peanut
# date : 2025/3/7


# demo1 使用内置函数len
str1 = "runoob"
print(len(str1))


# demo2 使用循环
def findLen(str2):
    counter = 0
    while str2[counter:]:
        counter += 1
    return counter


str_demo = "runoob"
print(findLen(str_demo))