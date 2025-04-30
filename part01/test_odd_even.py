# -*- coding: UTF-8 -*-

# filename : test_odd_even.py
# description : 判断奇数偶数
# author by : peanut
# date : 2025/2/25


num = int(input("请输入一个整数:"))

if (num % 2) == 0:
    print("{}是偶数".format(num))
else:
    print("{}是奇数".format(num))
