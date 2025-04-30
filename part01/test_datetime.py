# -*- coding: UTF-8 -*-

# filename : test_datetime.py
# description : datetime模块使用
# author by : peanut
# date : 2025/3/1

import datetime


# 获取昨天日期
def get_yesterday():
    # 获取当前日期
    today = datetime.date.today()
    # 获取昨天日期
    yesterday = today - datetime.timedelta(days=1)
    return yesterday


print(get_yesterday())
