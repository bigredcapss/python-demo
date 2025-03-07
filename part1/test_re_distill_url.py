# -*- coding: UTF-8 -*-

# filename : test_re_distill_url.py
# description : 使用正则表达式提取字符串中的 URL
# author by : peanut
# date : 2025/3/7

import re


def find(str1):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str1)
    return url


str_demo = 'trae 的网页地址为：https://www.trae.ai/，Cursor 的网页地址为：https://www.cursor.com'
print("Urls: ", find(str_demo))

