# -*- coding: UTF-8 -*-

# filename : test_fibonacci_sequence.py
# description : 斐波那契数列实现
# author by : peanut
# date : 2025/2/26

"""
    斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
"""

# 获取用户输入数据
n_terms = int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if n_terms <= 0:
    print("请输入一个正整数。")
elif n_terms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < n_terms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1


# 递归实现
def fibonacci_sequence(n):
    """
        斐波那契数列
        :param n: 斐波那契数列的第n项
        :return: 第n项的值
    """
    if n <= 0:
        return "输入的n必须大于0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
