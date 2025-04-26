# -*- coding: UTF-8 -*-

# filename : test_rwexcel.py
# description : 使用pandas和openyxl读写excel文件
# author by : peanut
# date : 2025/4/26


import pandas as pd

# 读取Excel文件
file_path = '2025-04-23-goup-chat-roomname-human-result-source-data.xlsx'
df = pd.read_excel(file_path)

# 显示前5行数据
print(df.head())

sheet_names = ['sheet_record_1', 'sheet_record_2']
dfs = pd.read_excel(file_path, sheet_names)

# 显示每个sheet的前5行数据
for sheet_name, df in dfs.items():
    print(f"Sheet Name: {sheet_name}")
    print(df.head())

# 写Excel文件
# 示例1-将 DataFrame 写入 Excel 文件
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 写入 Excel 文件
output_file_path = 'userInfo_file.xlsx'
df.to_excel(output_file_path, index=False)

# 示例2：将多个 DataFrame 写入不同的工作表
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['David', 'Emma', 'Frank'],
    'Age': [28, 27, 29],
    'City': ['Paris', 'Tokyo', 'Rome']
}
df2 = pd.DataFrame(data2)

# 写入Excel文件的不同工作表
with pd.ExcelWriter("output_file.xlsx", engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=True)

# 示例 3：读取特定列
columns = ['Name', 'Age']
df = pd.read_excel(output_file_path, usecols=columns)
print(df.head())

# 示例 4：读取特定行
rows = [0, 1, 2]
df = pd.read_excel(file_path, skiprows=rows)
print(df.head())
