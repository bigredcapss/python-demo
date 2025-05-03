# -*- coding: UTF-8 -*-

# filename : test_requests.py
# description : 使用requests
# author by : peanut
# date : 2025/4/13


import requests

"""
    Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
    更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。使用前需要先安装该模块
    pip install requests
"""

r = requests.get('https://liaoxuefeng.com/books/python/third-party-modules/requests/index.html')
print(r.status_code)
print(r.content)
print(r.encoding)
print(r.text)
print(r.json())



