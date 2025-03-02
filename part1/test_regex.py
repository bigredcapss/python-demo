# -*- coding: UTF-8 -*-

# filename : test_regex.py
# description : 使用正则表达式实现邮箱验证
# author by : peanut
# date : 2025/3/2

import re

"""
    在 Python 中，我们可以使用正则表达式来验证一个字符串是否符合邮箱的格式。
    邮箱通常包含用户名、@ 符号和域名部分。我们可以使用 re 模块来实现这一功能
"""


def validate_email(email):
    # 定义邮箱的正则表达式
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    # 使用 re.match 方法进行匹配
    if re.match(pattern, email):
        return True
    else:
        return False


# 测试邮箱
email = "example@example.com"
if validate_email(email):
    print(f"{email} 是一个有效的邮箱地址")
else:
    print(f"{email} 不是一个有效的邮箱地址")

