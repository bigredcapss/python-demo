# -*- coding: UTF-8 -*-

# filename : test_swap_var.py
# description : 交换变量
# author by : peanut
# date : 2025/2/24

x = input("请输入x的值: ")
y = input("请输入y的值: ")

# 方式1：通过临时变量temp交换变量
# temp = x
# x = y
# y = temp

# 方式2
x, y = y, x

print("交换后的x的值为:{}".format(x))
print("交换后的y的值为:{}".format(y))

