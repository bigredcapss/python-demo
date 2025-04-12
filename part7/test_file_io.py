# -*- coding: UTF-8 -*-

# filename : test_file_io.py
# description : Python基本的文件操作，包括 open，read，write：
# author by : peanut
# date : 2025/3/1


"""
    写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
"""


# with open('test.txt', 'w') as out_file:
#     out_file.write('Hello World!')
#     out_file.close()
#
# with open('test.txt', 'r') as in_file:
#     content = in_file.read()
#     print(content)
#     in_file.close()

try:
    f = open('/Users/wangen/py_workspace/python-demo/part3/test_decorator.py', 'r')
    print(f.read())
finally:
    # 检查文件对象是否已成功创建，若存在则关闭文件，确保资源释放
    if f:
        f.close()








