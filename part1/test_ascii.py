# -*- coding: UTF-8 -*-

# filename : test_ascii.py
# description : ascii与字符转换
# author by : peanut
# date : 2025/3/1

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

print(c + " 的ASCII 码为", ord(c))
print(a, " 对应的字符为", chr(a))

