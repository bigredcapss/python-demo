# -*- coding: UTF-8 -*-

# filename : test_re_search.py
# description : re.search方法
# author by : peanut
# date : 2025/3/8

"""
re.search 扫描整个字符串并返回第一个成功的匹配。
"""

import re

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")


