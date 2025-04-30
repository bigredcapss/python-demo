# -*- coding: UTF-8 -*-

# filename : test_prime.py
# description : 检测用户输入的数字是否为质数
# author by : peanut
# date : 2025/2/25

"""
    质数=一个大于1的自然数,除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等）
"""

num = int(input("请输入一个数字："))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            break
    else:
        print(num, "是质数")
else:
    print(num, "不是质数")

