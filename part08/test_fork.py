# -*- coding: UTF-8 -*-

# filename : test_fork.py
# description : xx
# author by : peanut
# date : 2025/4/13


import os


"""
    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
    普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
    然后，分别在父进程和子进程内返回。
    子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
    所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
    Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程

"""


print("Process (%s) start..." % os.getpid())
# Only works on Unix/Linux/macOS:
pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s)." % (os.getpid(), pid))