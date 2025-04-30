# -*- coding: UTF-8 -*-

# filename : test_multiplication-table.py
# description : 实现九九乘法表
# author by : peanut
# date : 2025/2/26

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, i * j), end='\t')
    print()

