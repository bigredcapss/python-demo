# -*- coding: UTF-8 -*-

# filename : test_todo_list.py
# description : 简单的任务清单
# author by : peanut
# date : 2025/3/7


# 简单的任务清单程序

# 创建一个空的任务列表
tasks = []

# 定义函数来添加任务
def add_task(task):
    tasks.append(task)
    print(f"任务 '{task}' 已添加.")

# 定义函数来显示任务列表
def show_tasks():
    if not tasks:
        print("任务清单是空的.")
    else:
        print("任务清单:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# 主程序循环
while True:
    print("\n选择一个选项:")
    print("1. 添加任务")
    print("2. 显示任务清单")
    print("3. 退出")

    choice = input("输入选项编号: ")

    if choice == "1":
        new_task = input("输入新任务: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("退出程序.")
        break
    else:
        print("无效的选项，请重新输入.")