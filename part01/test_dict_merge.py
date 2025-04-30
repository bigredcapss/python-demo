# -*- coding: UTF-8 -*-

# filename : test_dict_merge.py
# description : 字典合并
# author by : peanut
# date : 2025/3/7


# demo1 使用 update() 方法，第二个参数合并第一个参数
def dict_merge1(dict1, dict2):
    return (dict2.update(dict1))


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# 返回  None
print(dict_merge1(dict1, dict2))

# dict2 合并了 dict1
print(dict2)


# demo2  使用 **，函数将参数以字典的形式导入
def dict_merge2(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = dict_merge2(dict1, dict2)
print(dict3)




