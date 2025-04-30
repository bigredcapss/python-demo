# -*- coding: UTF-8 -*-

# filename : test_sum_array.py
# description : 计算数组元素之和
# author by : peanut
# date : 2025/3/2

"""
    定义一个整型数组，并计算元素之和。
    输入 : arr[] = {1, 2, 3}
    输出 : 6
    计算: 1 + 2 + 3 = 6
"""


"""
    单下划线 _sum：表示这个方法是内部使用的，不建议外部代码直接调用。
    虽然 Python 并不会阻止你从外部访问这个方法，但这是一种提示，告诉其他开发者这个方法不是公共接口的一部分
    
    双下划线 __method：如果使用双下划线开头，则会触发 Python 的名称改写机制（name mangling），使得该方法更难以被外部访问。
    不过这通常用于避免子类覆盖父类的方法，而不是简单的私有化
"""


# 定义函数，arr 为数组，n 为数组长度，可作为备用参数，这里没有用到
def _sum(arr, n):
    # 使用内置的 sum 函数计算
    return sum(arr)

# 数组元素
arr = [12, 3, 4, 15]

# 计算数组元素的长度
n = len(arr)

ans = _sum(arr, n)

# 输出结果
print('数组元素之和为', ans)






