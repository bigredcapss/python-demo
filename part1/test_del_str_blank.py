# -*- coding: UTF-8 -*-

# filename : test_del_str_blank.py
# description : 删除字符串首尾的空格
# author by : peanut
# date : 2025/3/7

import re


# demo1 要删除字符串首尾的空格可以使用 strip() 方法
original_string = "   这是一个带有空格的字符串   "
stripped_string = original_string.strip()
print(stripped_string)


# demo2
"""
    如果字符串中有 \n 等字符，并且您只想删除空格，则需要在 strip() 方法上显式指定它
"""
my_string1 = " \nPython "

print(my_string1.strip(" "))



# demo3 使用正则
my_string2  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string2)

print(output)


