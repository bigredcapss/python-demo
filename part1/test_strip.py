# -*- coding: UTF-8 -*-

# filename : test_strip.py
# description : 删除字符串首尾的空格
# author by : peanut
# date : 2025/3/2

import re

"""
    Python 要删除字符串首尾的空格可以使用 strip() 方法。
    strip() 方法将删除字符串开头和结尾的所有空格（包括空格、制表符和换行符）
"""


# strip()
original_str = "   Hello World   "
print("原始字符串：", original_str)
print("删除首尾空格后的字符串：", original_str.strip())


# strip()指定字符
my_string = " \nPython "
print(my_string.strip(" "))


# 使用正则表达式来删除字符串首尾的空格
my_string = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)
print(output)


"""
    lstrip() -- 删除字符串开头的空格。
    rstrip() -- 删除字符串结尾的空格。
"""
original_string = "   这是一个带有空格的字符串   "
left_stripped_string = original_string.lstrip()  # 删除开头的空格
right_stripped_string = original_string.rstrip()  # 删除结尾的空格

print(left_stripped_string)
print(right_stripped_string)





