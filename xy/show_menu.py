def show_menu():
    """
    显示菜单
    """
    print("\n任务管理系统")
    print("1. 添加任务")
    print("2. 标记任务为已完成")
    print("3. 删除任务")
    print("4. 查看所有任务")
    print("5. 退出系统")


def add_task(tasks):
    """
    添加新任务
    :param tasks: 当前任务列表
    """
    task_name = input("请输入任务名称：")
    tasks.append({"name": task_name, "completed": False})
    print(f"任务 '{task_name}' 已添加！")


def complete_task(tasks):
    """
    标记任务为已完成
    :param tasks: 当前任务列表
    """
    show_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("请输入已完成任务的编号：")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print(f"任务 '{tasks[task_num]['name']}' 已标记为完成！")
    else:
        print("任务编号无效！")


def delete_task(tasks):
    """
    删除任务
    :param tasks: 当前任务列表
    """
    show_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("请输入要删除任务的编号：")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"任务 '{removed_task['name']}' 已删除！")
    else:
        print("任务编号无效！")


def show_tasks(tasks):
    """
    显示所有任务
    :param tasks: 当前任务列表
    """
    if not tasks:
        print("当前没有任务！")
        return
    print("\n当前任务列表：")
    for i, task in enumerate(tasks, 1):
        status = "完成" if task["completed"] else "未完成"
        print(f"{i}. {task['name']} [{status}]")


def main():
    """
    主函数，运行任务管理系统
    """
    tasks = []  # 用于存储任务的列表
    while True:
        show_menu()
        choice = input("请输入操作编号：")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            print("感谢使用任务管理系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")


if __name__ == "__main__":
    main()
