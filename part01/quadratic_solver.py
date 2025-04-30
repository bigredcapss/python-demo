# -*- coding: UTF-8 -*-

# # 导入 cmath 模块，支持复数运算
# import cmath
#
# # filename : quadratic_solver.py
# # description : 求解二次方程 ax**2 + bx + c = 0
# # author by : peanut
# # date : 2025/2/23
#
# """
#     二次方程的形式为：ax2+bx+c=0。
#     其解可以通过求判别式 Δ=b^2-4ac
#     如果 Δ > 0，方程有两个实数根。
#     如果 Δ = 0，方程有一个实数根（双重根）。
#     如果 Δ < 0，方程没有实数根，但有两个复数根。
# """
#
#
# def get_float_input(prompt):
#     """
#         获取用户输入的浮点数，并处理非法输入。
#         :param prompt: 提示信息
#         :return: 用户输入的浮点数
#     """
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("请输入有效的数字!")
#
#
# def solve_quadratic(a, b, c):
#     """
#         计算二次方程的解。
#         :param a: 二次项系数
#         :param b: 一次项系数
#         :param c: 常数项
#         :return: 二次方程的两个解
#     """
#     discriminant = b**2 - 4*a*c  # 计算判别式
#     root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
#     root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
#     return root1, root2
#
#
# def main():
#     print("求解二次方程 ax^2 + bx + c = 0")
#
#     # 获取用户输入
#     a = get_float_input("请输入二次项系数 a（a ≠ 0）：")
#     while a == 0:
#         print("二次方程的二次项系数 a 不能为 0！")
#         a = get_float_input("请重新输入二次项系数 a（a ≠ 0）：")
#
#     b = get_float_input("请输入一次项系数 b：")
#     c = get_float_input("请输入常数项 c：")
#
#     # 计算并输出结果
#     root1, root2 = solve_quadratic(a, b, c)
#     print(f"方程的解为：{root1} 和 {root2}")
#
#
# if __name__ == "__main__":
#     main()

import math
import cmath


def solve_quadratic(a, b, c):
    """
    求解二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的解（可能为实数或复数）
    """
    if a == 0:
        # 非二次方程处理
        if b == 0:
            return "无解" if c != 0 else "方程有无穷多个解"
        return f"方程是线性方程，解为 x = {-c / b}"

    # 计算判别式
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        # 两个实数根
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"方程有两个实数根：x1 = {root1}, x2 = {root2}"
    elif delta == 0:
        # 一个实数根
        root = -b / (2 * a)
        return f"方程有一个双重实数根：x = {root}"
    else:
        # 两个复数根
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return f"方程有两个复数根：x1 = {root1}, x2 = {root2}"


# 示例调用
a, b, c = 1, -3, 2
result = solve_quadratic(a, b, c)
print(result)