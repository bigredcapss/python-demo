# -*- coding: UTF-8 -*-

# filename : test_leap_year.py
# description : 判断是否是闰年
# author by : peanut
# date : 2025/2/25

"""
    闰年判定条件：闰年=可被4整除，但不可被100整除 或者可被400整除
"""


year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))

