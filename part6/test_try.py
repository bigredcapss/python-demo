# -*- coding: UTF-8 -*-

# filename : test_try.py
# description : try-https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# author by : peanut
# date : 2025/4/12


try:
    print("try...")
    r = 10 / 0
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print("finally...")
print("END")