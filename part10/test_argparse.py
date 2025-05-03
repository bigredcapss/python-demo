# -*- coding: UTF-8 -*-

# filename : test_argparse.py
# description : 使用argparse解析命令行参数
# author by : peanut
# date : 2025/5/2


"""
    在命令行程序中，经常需要获取命令行参数。Python内置的sys.argv保存了完整的参数列表，
    我们可以从中解析出需要的参数。

    我们不必捕获异常，parse_args()非常方便的一点在于，如果参数有问题，则它打印出错误信息后，结束进程；
    如果参数是-h，则它打印帮助信息后，结束进程。只有当参数全部有效时，才会返回一个NameSpace对象，
    获取对应的参数就把参数名当作属性获取，非常方便。可见，使用argparse后，解析参数的工作被大大简化了，
    我们可以专注于定义参数，然后直接获取到有效的参数输入。

    为了简化参数解析，我们可以使用内置的argparse库，定义好各个参数类型后，它能直接返回有效的参数。

"""

import sys
import argparse


# print("命令行参数列表:", sys.argv)

# if len(sys.argv) > 2:
#     print("第一个参数:", sys.argv[1])
#     print("第二个参数:", sys.argv[2])
# else:
#     print("请提供至少两个命令行参数")


# 使用argparse解析命令行参数
def main():
    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='test_argparse', # 程序名
        description='test argparse', # 描述
        epilog='Copyright(r), 2025' # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')


    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()














