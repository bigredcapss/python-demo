# -*- coding: UTF-8 -*-

# filename : test_remove_char.py
# description : 移除字符串中的指定字符
# author by : peanut
# date : 2025/3/7


test_str = "Runoob"

# 输出原始字符串
print("原始字符串为 : " + test_str)

# 移除第三个字符 n
new_str = ""

for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("字符串移除后为 : " + new_str)