# -*- coding: UTF-8 -*-

# filename : test_udp_server.py
# description : 使用socket创建udp服务端响应客户端请求
# author by : peanut
# date : 2025/5/2

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 发送数据:
    s.sendto(b'Hello, %s!' % data, addr)


