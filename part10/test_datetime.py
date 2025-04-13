# -*- coding: UTF-8 -*-

# filename : test_datetime.py
# description : 使用datetime
# author by : peanut
# date : 2025/4/13

from datetime import datetime

"""
    datetime是Python处理日期和时间的标准库。
"""


# 获取当前日期和时间
now = datetime.now()
print(now)

# 获取指定日期与时间
dt = datetime(2025, 4, 13, 12, 20,30,125)
print(dt)




