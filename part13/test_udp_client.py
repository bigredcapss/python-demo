# -*- coding: UTF-8 -*-

# filename : test_udp_client.py
# description : 使用socket创建udp客户端请求udp服务端
# author by : peanut
# date : 2025/5/2


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()



