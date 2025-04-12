# -*- coding: UTF-8 -*-

# filename : test_re_match.py
# description : re.match函数
# author by : peanut
# date : 2025/3/8

import re


"""
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 None。
    函数语法
    1、re.match(pattern, string, flags=0)

    匹配成功 re.match 方法返回一个匹配的对象，否则返回 None。
"""

# 使用 Python 的 re.match 函数对字符串进行匹配，并输出匹配结果的起始和结束位置
# 如果目标字符串不是以 'www' 开头（例如 'http://www.runoob.com'），re.match 将返回 None，调用 .span() 会引发错误。
print(re.match('www', 'www.runoob.com').span())

# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))


line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)


# 使用 group(num) 或 groups() 匹配对象函数来获取匹配的表达式
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
