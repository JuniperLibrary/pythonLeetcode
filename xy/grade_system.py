"""
需求描述：
创建一个学生成绩管理系统，支持以下功能：
1. 添加学生及其成绩。
2. 删除学生信息。
3. 修改学生成绩。
4. 查询某个学生的成绩。
5. 显示所有学生及其成绩。
6. 显示平均分、最高分和最低分。
7. 退出系统。

实现方式：
使用 Python 的字典存储学生和成绩信息。
通过交互式菜单实现用户与系统的交互。
"""

class GradeSystem:
    def __init__(self):
        """初始化成绩系统，创建一个空的学生成绩字典"""
        self.grades = {}

    def add_student(self, name, score):
        """
        添加学生及其成绩。
        :param name: 学生姓名。
        :param score: 学生成绩。
        功能：
        - 检查学生是否已经存在。
        - 将学生及其成绩存入字典。
        """
        if name in self.grades:
            print(f"学生 {name} 已存在，无法重复添加！")
        else:
            self.grades[name] = score
            print(f"成功添加学生 {name}，成绩为 {score}！")

    def remove_student(self, name):
        """
        删除学生信息。
        :param name: 学生姓名。
        功能：
        - 检查学生是否存在。
        - 从字典中删除学生信息。
        """
        if name in self.grades:
            del self.grades[name]
            print(f"成功删除学生 {name}！")
        else:
            print(f"学生 {name} 不存在，无法删除！")

    def update_score(self, name, score):
        """
        修改学生成绩。
        :param name: 学生姓名。
        :param score: 新成绩。
        功能：
        - 检查学生是否存在。
        - 更新字典中的学生成绩。
        """
        if name in self.grades:
            self.grades[name] = score
            print(f"成功更新学生 {name} 的成绩为 {score}！")
        else:
            print(f"学生 {name} 不存在，无法修改成绩！")

    def query_score(self, name):
        """
        查询学生成绩。
        :param name: 学生姓名。
        功能：
        - 检查学生是否存在。
        - 输出学生的成绩。
        """
        if name in self.grades:
            print(f"学生 {name} 的成绩为：{self.grades[name]}！")
        else:
            print(f"学生 {name} 不存在！")

    def show_all_students(self):
        """显示所有学生及其成绩。"""
        if not self.grades:
            print("当前没有学生记录！")
        else:
            print("学生成绩列表：")
            for name, score in self.grades.items():
                print(f"{name}: {score}")

    def show_statistics(self):
        """
        显示平均分、最高分和最低分。
        功能：
        - 计算并输出平均分、最高分和最低分。
        - 如果没有学生记录，提示用户。
        """
        if not self.grades:
            print("当前没有学生记录，无法统计！")
        else:
            scores = list(self.grades.values())
            average = sum(scores) / len(scores)
            highest = max(scores)
            lowest = min(scores)
            print(f"平均分：{average:.2f}，最高分：{highest}，最低分：{lowest}")


def main():
    """主函数，提供用户交互功能"""
    system = GradeSystem()

    while True:
        print("\n请选择操作：")
        print("1. 添加学生及成绩")
        print("2. 删除学生信息")
        print("3. 修改学生成绩")
        print("4. 查询学生成绩")
        print("5. 显示所有学生及成绩")
        print("6. 显示平均分、最高分和最低分")
        print("7. 退出系统")

        choice = input("请输入您的选择（1/2/3/4/5/6/7）：")

        if choice == "1":
            name = input("请输入学生姓名：")
            score = float(input("请输入学生成绩："))
            system.add_student(name, score)
        elif choice == "2":
            name = input("请输入要删除的学生姓名：")
            system.remove_student(name)
        elif choice == "3":
            name = input("请输入要修改成绩的学生姓名：")
            score = float(input("请输入新的成绩："))
            system.update_score(name, score)
        elif choice == "4":
            name = input("请输入要查询的学生姓名：")
            system.query_score(name)
        elif choice == "5":
            system.show_all_students()
        elif choice == "6":
            system.show_statistics()
        elif choice == "7":
            print("感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")


if __name__ == "__main__":
    main()
