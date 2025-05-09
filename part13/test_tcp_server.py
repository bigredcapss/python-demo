# -*- coding: UTF-8 -*-

# filename : test_tcp_server.py
# description : 使用socket创建tcp服务端响应客户端请求
# author by : peanut
# date : 2025/5/2



import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 绑定监听端口
s.bind(('127.0.0.1',9999))

# 开始监听端口,并指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

# 循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


















