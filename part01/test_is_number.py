# -*- coding: UTF-8 -*-

# filename : test_is_number.py
# description : 判断字符串是否为数字
# author by : peanut
# date : 2025/2/25

"""
    Python isdigit() 方法检测字符串是否只由数字组成。
    Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象
"""


def is_number(s):
    # 方式1
    try:
        float(s)
        return True
    except ValueError:
        pass

    # # 方式2
    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (ValueError, TypeError):
    #     pass
    #
    # # 方式3
    # try:
    #     print(s.isdigit())
    # except AttributeError:
    #     pass
    #
    # # 方式4
    # try:
    #     print(s.isnumeric())
    # except AttributeError:
    #     pass

    return False


# 测试验证
print(is_number('5'))
print(is_number('he'))
print(is_number('1.3'))
print(is_number('-3.25'))
print(is_number('1e3'))





