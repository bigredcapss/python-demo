# -*- coding: UTF-8 -*-

# filename : temperature_convert.py
# description : 摄氏温度转华氏温度
# author by : peanut
# date : 2025/2/24

"""
    计算公式: 摄氏温度 * 1.8 = 华氏温度 - 32
"""

celsius = float(input("请输入摄氏温度："))

# 计算华氏温度
fahrenheit = celsius * 1.8 + 32

print("%0.1f 摄氏温度转换为华氏温度为：%0.1f" %(celsius, fahrenheit))