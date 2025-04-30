# -*- coding: UTF-8 -*-

# filename : test_str_split_reverse.py
# description : 字符串切片及翻转
# author by : peanut
# date : 2025/3/7


def rotate(str, d):
    l_first = str[0: d]
    l_second = str[d:]
    r_first = str[0: len(str) - d]
    r_second = str[len(str) - d:]

    print("头部切片翻转 : ", (l_second + l_first))
    print("尾部切片翻转 : ", (r_second + r_first))


if __name__ == "__main__":
    str_demo = 'Runoob'
    d = 2  # 截取两个字符
    rotate(str_demo, d)
