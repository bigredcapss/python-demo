# -*- coding: UTF-8 -*-

# filename : test_output_range_number.py
# description : 输入指定范围的素数（质数）
# author by : peanut
# date : 2025/2/26

lower = int(input("输入区间最小值："))
upper = int(input("输入区间最大值："))

for num in range(lower, upper + 1):
    # 素数大于1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
