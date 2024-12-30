"""
需求描述：
创建一个银行账户管理系统，支持以下功能：
1. 存款功能：用户可以将指定金额存入账户。
2. 取款功能：用户可以从账户中取出指定金额，余额不足时提示错误。
3. 查询余额：用户可以随时查看账户余额。
4. 查看交易记录：用户可以查看存取款的历史记录。
5. 退出系统：用户可以选择退出系统，结束程序运行。

扩展任务：
1. 增加交易记录查询功能，显示用户的存款和取款历史记录。
2. 添加用户身份验证功能，通过密码保护账户。
3. 支持多账户管理，允许用户创建多个账户并选择操作的账户。

实现方式：
使用 Python 面向对象编程（OOP），以类的形式封装账户的相关信息和操作逻辑。
通过交互式的菜单循环实现用户与系统的交互。
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        """
        初始化银行账户。
        :param owner: 账户所有人。
        :param balance: 初始余额，默认为0。
        功能：
        - 设置账户所有人。
        - 初始化账户余额。
        - 创建一个空的交易历史列表。
        """
        self.owner = owner
        self.balance = balance
        self.transaction_history = []  # 记录交易历史

    def deposit(self, amount):
        """
        存款操作。
        :param amount: 存入的金额。
        功能：
        - 检查金额是否合法（大于0）。
        - 将金额增加到账户余额中。
        - 将存款记录添加到交易历史。
        - 输出存款成功的信息和当前余额。
        """
        if amount <= 0:
            print("存款金额必须大于0！")
            return
        self.balance += amount
        self.transaction_history.append(f"存款: +{amount} 元")
        print(f"成功存入 {amount} 元！当前余额：{self.balance} 元")

    def withdraw(self, amount):
        """
        取款操作。
        :param amount: 取款金额。
        功能：
        - 检查金额是否合法（大于0）。
        - 检查账户余额是否足够取款。
        - 从账户余额中扣除金额。
        - 将取款记录添加到交易历史。
        - 输出取款成功的信息和当前余额。
        """
        if amount <= 0:
            print("取款金额必须大于0！")
            return
        if amount > self.balance:
            print("余额不足！取款失败。")
            return
        self.balance -= amount
        self.transaction_history.append(f"取款: -{amount} 元")
        print(f"成功取出 {amount} 元！当前余额：{self.balance} 元")

    def check_balance(self):
        """
        查询余额。
        功能：
        - 输出当前账户余额。
        """
        print(f"当前余额为：{self.balance} 元")

    def show_transaction_history(self):
        """
        显示交易历史。
        功能：
        - 检查交易历史是否为空。
        - 输出每一条交易记录。
        """
        if not self.transaction_history:
            print("暂无交易记录。")
        else:
            print("交易记录如下：")
            for record in self.transaction_history:
                print(record)


def main():
    """
    主函数，提供用户交互功能。
    功能：
    - 提示用户输入名字并创建账户。
    - 提供操作菜单，用户可以选择存款、取款、查询余额、查看交易记录或退出系统。
    - 根据用户选择调用对应的功能。
    - 当用户选择退出时，结束程序。
    """
    print("欢迎使用银行账户管理系统！")
    name = input("请输入您的名字：")
    account = BankAccount(name)

    while True:
        print("\n请选择操作：")
        print("1. 存款")
        print("2. 取款")
        print("3. 查询余额")
        print("4. 查看交易记录")
        print("5. 退出系统")
        choice = input("请输入您的选择（1/2/3/4/5）：")

        if choice == "1":
            amount = float(input("请输入存款金额："))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("请输入取款金额："))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transaction_history()
        elif choice == "5":
            print("感谢使用银行账户管理系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")


if __name__ == "__main__":
    main()
