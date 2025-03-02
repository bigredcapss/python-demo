# -*- coding: UTF-8 -*-

# filename : test_calendar.py
# description : 生成指定日期的日历并获取每个月的天数
# author by : peanut
# date : 2025/3/1

import calendar


# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

print(calendar.month(yy, mm))

# 计算每个月的天数
monthRange = calendar.monthrange(2016,9)
print(monthRange)


# def generate_calendar(year, month):
#     # 创建日历对象
#     cal = calendar.TextCalendar()
#
#     # 生成指定日期的日历
#     calendar_text = cal.formatmonth(year, month)
#
#     return calendar_text
#
#
# if __name__ == '__main__':
#     year = 2025
#     month = 3
#
#     calendar_text = generate_calendar(year, month)
#     print(calendar_text)

