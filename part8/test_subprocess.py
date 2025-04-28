# -*- coding: UTF-8 -*-

# filename : test_subprocess.py
# description : 使用subprocess模块使用子进程
# author by : peanut
# date : 2025/4/28

"""
    很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
    subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
    如果子进程还需要输入，则可以通过communicate()方法输入。
    subprocess.Popen 类创建了一个新的子进程来运行 nslookup 命令，并配置了子进程的标准输入（stdin）、标准输出（stdout）和
    标准错误（stderr），以便在父进程中进行控制和处理。
    nslookup用于查询DNS信息，包括域名的IP地址等。

"""


import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

