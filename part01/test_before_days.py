# -*- coding: UTF-8 -*-

# filename : test_before_days.py
# description : 获取几天前的时间
# author by : peanut
# date : 2025/3/7


"""
    计算几天前并转换为指定格式。
"""

import time
import datetime

# demo1
# 先获得时间数组格式的日期
threeDayAgo1 = (datetime.datetime.now() - datetime.timedelta(days=3))
# 转换为时间戳
timeStamp1 = int(time.mktime(threeDayAgo1.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo1.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)


# demo2
# 给定时间戳
timeStamp2 = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp2)
threeDayAgo2 = dateArray - datetime.timedelta(days=3)
print(threeDayAgo2)


