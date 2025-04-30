# -*- coding: UTF-8 -*-

# filename : test_calculator.py
# description : 实现简单计算器
# author by : peanut
# date : 2025/3/1

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


# 方案1
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("输入你的选择(1/2/3/4):")

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("无效输入")


# 方案2
while True:
    print("选择运算：")
    print("1、相加")
    print("2、相减")
    print("3、相乘")
    print("4、相除")

    choice = input("输入选项编号: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("输入第一个数: "))
        num2 = float(input("输入第二个数: "))

        if choice == '1':
            print(f"结果: {add(num1, num2)}")
        elif choice == '2':
            print(f"结果: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"结果: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"结果: {divide(num1, num2)}")
    elif choice == '5':
        print("退出程序.")
        break
    else:
        print("无效的选项，请重新输入.")
