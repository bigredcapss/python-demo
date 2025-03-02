# -*- coding: UTF-8 -*-

# filename : test_list.py
# description : list常用操作
# author by : peanut
# date : 2025/3/1


# list定义
list1 = ["a", "b", "mpilgrim", "z", "example"]

# list索引访问
# print(list1)
# print(list1[1])
#
# print(list1[-1])
# print(list1[0:-3])


# list添加元素
# list1[2] = "m"
# print(list1)
# list1.append("zab")
# print(list1)
# list1.extend(["first", "second"])
# print(list1)
# list1.insert(2, "new")
# print(list1)

# list的搜索
# print(list1.index("c"))
# print(list1.index("new"))  # 访问一个不存在的元素会报错


# list删除元素
# print(list1.remove("c"))
# print(list1.remove("new"))  # list 中没有找到值, Python 会引发一个异常
# print(list1.pop("a"))  # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。


# list运算符
print(list1 * 2)
print(list1 + ["wang", "zhang"])


# 使用join链接list成为字符串
"""
    join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
"""
print(";".join(list1))


# list 分割字符串
str1 = "server=mpilgrim;uid=sa;database=master;pwd=secret"
print(str1.split(";"))


# list的映射解析
list2 = [elem*2 for elem in list1]
print(list2)


# list过滤
print([elem for elem in list1 if len(elem) > 1])








