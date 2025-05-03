# -*- coding: UTF-8 -*-

# filename : test_struct.py
# description : 使用struct模块解决bytes和其他二进制数据类型的转换
# author by : peanut
# date : 2025/5/2


"""
    Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。
    而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
    struct模块提供了pack()和unpack()函数，用于处理bytes和其他二进制数据类型的转换。
"""


import struct

# 传统做法==>将一个32位整数和4个字节的bytes数据转换为bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff


"""
    struct的pack函数把任意数据类型变成bytes
    '>I'的意思是：
    >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    后面的参数个数要和处理指令一致。
"""
bs = struct.pack('>I', 10240099)
print(bs)


"""
    struct.unpack()函数把bytes变成相应的数据类型：
    根据>IH，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
"""
bs = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(bs)




