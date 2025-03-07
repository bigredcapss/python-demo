# -*- coding: UTF-8 -*-

# filename : test_dict_sort.py
# description : 按键(key)或值(value)对字典进行排序
# author by : peanut
# date : 2025/3/7


"""
    给定一个字典，然后按键(key)或值(value)对字典进行排序。
    sorted(key_value) 是 Python 内置函数 sorted() 的用法，用于对可迭代对象进行排序。
    在这里，key_value 是一个字典，sorted() 默认会按字典的键（key）进行排序。
    返回值是一个列表，包含字典中所有键的升序排序结果
"""


def dict_sort():

    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序:")

    # sorted(key_value) 返回重新排序的列表
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # 调用函数
    dict_sort()


# 主函数
if __name__ == "__main__":
    main()




