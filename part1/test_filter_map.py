# -*- coding: UTF-8 -*-

# filename : test_filter_map.py
# description : 使用 filter 和 map 函数处理数据
# author by : peanut
# date : 2025/3/2


"""
    在 Python 中，filter 和 map 是两个非常有用的内置函数，它们可以帮助我们以函数式编程的方式处理数据。
    filter 函数用于过滤序列中的元素，而 map 函数用于对序列中的每个元素应用一个函数
"""

# 定义一个包含数字的列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 filter 函数过滤出偶数
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# 使用 map 函数将偶数乘以 2
doubled_even_numbers = map(lambda x: x * 2, even_numbers)

# 将结果转换为列表并打印
result = list(doubled_even_numbers)
print(result)





