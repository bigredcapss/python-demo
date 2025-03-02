# -*- coding: UTF-8 -*-

# filename : test_lcm.py
# description : 求最小公倍数
# author by : peanut
# date : 2025/3/1

def lcm_function1(a, b):
    """
    求最小公倍数

    参数:
    a (int): 第一个数
    b (int): 第二个数

    返回值:
    int: 最小公倍数
    """

    # 获取两个数的最大公约数
    import test_hcf
    gcd = test_hcf.hcf_function(a, b)

    # 最小公倍数等于两个数的乘积除以最大公约数
    lcm = a * b // gcd

    return lcm


def lcm_function2(a, b):

    # 获取最大的数
    if a > b:
        max_num = a
    else:
        max_num = b

    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1

    return max_num


# 获取用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最小公倍数为", lcm_function1(num1, num2))




