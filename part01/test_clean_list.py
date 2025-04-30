# -*- coding: UTF-8 -*-

# filename : test_clean_list.py
# description : 清空列表
# author by : peanut
# date : 2025/3/5


def clean_list(list_name):
    """
    清空列表
    :param list_name: 列表名
    :return:
    """
    list_name.clear()


list1 = [6, 0, 4, 1]
print('清空前:', list1)

list1.clear()
print('清空后:', list1)