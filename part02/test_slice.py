# -*- coding: UTF-8 -*-

# filename : test_slice.py
# description : 切片操作[初始索引:结束索引:步长]
# author by : peanut
# date : 2025/4/12


L = ["Michael", "Sarah", "Tracy", "Bob", "Jack"]

print("L[0:3] =", L[0:3])
print("L[:3] =", L[:3])
print("L[1:3] =", L[1:3])
print("L[-2:] =", L[-2:])

R = list(range(100))
print("R[:10] =", R[:10])
print("R[-10:] =", R[-10:])
print("R[10:20] =", R[10:20])
print("R[:10:2] =", R[:10:2])
print("R[::5] =", R[::5])

S = "hello, world"
print("S[:5] =", S[:5])
print("S[7:] =", S[7:])