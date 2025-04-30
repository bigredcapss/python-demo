# -*- coding: UTF-8 -*-

# filename : test_exec.py
# description : 将字符串作为代码执行
# author by : peanut
# date : 2025/3/2

"""
    给定一个字符串代码，然后使用 exec() 来执行字符串代码
"""


def exec_code():
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)


exec_code()