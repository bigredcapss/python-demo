# -*- coding: UTF-8 -*-

# filename : test_factorial.py
# description : 阶乘运算
# author by : peanut
# date : 2025/2/26

"""
    整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
"""

num = int(input("请输入一个数字："))

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
