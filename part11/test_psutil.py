# -*- coding: UTF-8 -*-

# filename : test_psutil.py
# description : 使用psutil检测系统信息
# author by : peanut
# date : 2025/5/2


"""
    用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
    要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
    在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，
    它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
"""

import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_percent(interval=1))
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.net_io_counters())
