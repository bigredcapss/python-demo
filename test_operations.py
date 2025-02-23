# -*- coding: UTF-8 -*-
import math

# filename : test_operations.py
# description : 数学运算
# author by : peanut
# date : 2025/2/23

print('----------------求和运算----------------')

# 用户输入
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')

# 求和
sum_value = float(num1) + float(num2)

print('数字 {0} 和数字 {1} 相加的结果为: {2} '.format(num1,num2,sum_value))
print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
print('----------------求和运算----------------')


print('----------------平方根运算----------------')

# 用户输入
num3 = float(input('请输入第一个数字：'))

# 求正数的平方根
num_sqrt = num3 ** 0.5

print('{0} 的平方根为 {1}'.format(num3,num_sqrt))
print('%0.3f 的平方根为 %0.3f'%(num3,num_sqrt))

# 求平方根
num_math_sqrt = math.sqrt(num3)

print('{0} 的平方根为 {1}'.format(num3,num_math_sqrt))

print('----------------平方根运算----------------')


print('----------------运算----------------')

# 用户输入
num3 = float(input('请输入第一个数字：'))

# 求正数的平方根
num_sqrt = num3 ** 0.5

print('{0} 的平方根为 {1}'.format(num3,num_sqrt))
print('%0.3f 的平方根为 %0.3f'%(num3,num_sqrt))

print('----------------平方根运算----------------')


