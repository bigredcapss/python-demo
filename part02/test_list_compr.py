# -*- coding: UTF-8 -*-

# filename : test_list_compr.py
# description : 列表生成式 [表达式 for x in 可迭代对象 筛选条件]
# author by : peanut
# date : 2025/4/12


print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in "ABC" for n in "XYZ"])

d = {"x": "A", "y": "B", "z": "C"}
print([k + "=" + v for k, v in d.items()])

L = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in L])