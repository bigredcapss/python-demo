# -*- coding: UTF-8 -*-

# filename : test_mysql.py
# description : python连接mysql
# author by : peanut
# date : 2025/3/16


#import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root123456",
#     auth_plugin='mysql_native_password'  # 指定认证插件
# )

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="root123456");

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)



