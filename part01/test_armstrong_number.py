# -*- coding: UTF-8 -*-

# filename : test_armstrong_number.py
# description : 检测阿姆斯特朗数
# author by : peanut
# date : 2025/2/28

"""
    如果一个 n 位正整数等于其各位数字的 n 次方之和，则称该数为阿姆斯特朗数。 例如 1^3 + 5^3 + 3^3 = 153。
    1000 以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""

# 获取用户输入的数字
num = int(input("请输入一个数字: "))

# 初始化变量 sum1
sum1 = 0
# 指数
n = len(str(num))

# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum1 += digit ** n
    temp //= 10

# 输出结果
if num == sum1:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")


"""
    获取指定范围内的阿姆斯特朗数
"""
# 获取用户输入数字
lower = int(input("最小值: "))
upper = int(input("最大值: "))

for num in range(lower, upper + 1):
    # 初始化 sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)
