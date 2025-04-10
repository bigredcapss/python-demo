# -*- coding: UTF-8 -*-

# filename : test_file_io.py
# description : Python基本的文件操作，包括 open，read，write：
# author by : peanut
# date : 2025/3/1

with open('test.txt', 'w') as out_file:
    out_file.write('Hello World!')
    out_file.close()

with open('test.txt', 'r') as in_file:
    content = in_file.read()
    print(content)
    in_file.close()








