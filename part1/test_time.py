# -*- coding: UTF-8 -*-

# filename : test_time.py
# description : 实现秒表功能
# author by : peanut
# date : 2025/3/2

import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')

while True:
    input("")  # 等待用户按下回车开始计时
    start_time = time.time()  # 记录开始时间
    print('开始计时...')

    try:
        while True:
            elapsed_time = round(time.time() - start_time, 0)  # 计算经过的时间
            print(f'计时: {elapsed_time} 秒', end="\r")  # 覆盖上次输出
            time.sleep(1)
    except KeyboardInterrupt:  # 捕捉 Ctrl + C 中断信号
        end_time = time.time()  # 记录结束时间
        total_time = round(end_time - start_time, 2)
        print(f'\n计时结束，总共时间为: {total_time} 秒')
        break
