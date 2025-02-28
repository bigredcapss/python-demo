# -*- coding: UTF-8 -*-

import random

# filename : test_random.py
# description : random模块随机数测试
# author by : peanut
# date : 2025/2/24

# 返回一个介于 0.0 和 1.0 之间的随机小数
random_num = random.random()
print(random_num)

# 返回一个介于 a 和 b 之间的整数（包括 a 和 b）
randint_num = random.randint(1,10)
print(randint_num)

# 从序列中随机选择一个元素
list1 = [1, 2, 3, 4, 9, 8]
random_element = random.choices(list1)
print(random_element)

# 将序列中的元素进行随机排序
list2 = [1, 2, 3, 4, 5]
random.shuffle(list2)
print(list2)

