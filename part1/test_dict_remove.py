# -*- coding: UTF-8 -*-

# filename : test_dict_remove.py
# description : 移除字典点键值(key/value)对
# author by : peanut
# date : 2025/3/7


"""
    给定一个字典， 移除字典点键值(key/value)对。
"""


# demo1 使用 del 移除
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# 输出原始的字典
print("字典移除前 : " + str(test_dict))

# 使用 del 移除 Zhihu
del test_dict['Zhihu']

# 输出移除后的字典
print("字典移除后 : " + str(test_dict))

# 移除没有的 key 会报错
# del test_dict['Baidu']


# demo2 使用 pop() 移除
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# 输出原始的字典
print("字典移除前 : " + str(test_dict))

# 使用 pop 移除 Zhihu
removed_value = test_dict.pop('Zhihu')

# 输出移除后的字典
print("字典移除后 : " + str(test_dict))

print("移除的 key 对应的 value 为 : " + str(removed_value))

print('\r')

# 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息
removed_value = test_dict.pop('Baidu', '没有该键(key)')

# 输出移除后的字典
print("字典移除后 : " + str(test_dict))
print("移除的值为 : " + str(removed_value))


# demo3 使用 items() 移除
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# 输出原始的字典
print("字典移除前 : " + str(test_dict))

# 使用 pop 移除 Zhihu
new_dict = {key: val for key, val in test_dict.items() if key != 'Zhihu'}

# 输出移除后的字典
print("字典移除后 : " + str(new_dict))