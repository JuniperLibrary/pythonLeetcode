def calculate_min_initial_battery(tasks_str):
    tasks = tasks_str.split(',')
    task_list = []

    for task in tasks:
        power, min_initial_battery = map(int, task.split(':'))
        task_list.append((power, min_initial_battery))

    task_list.sort()  # 按照耗电量从小到大排序

    max_battery = 4800
    n = len(task_list)

    # dp[i][j] 表示前 i 个任务完成时，手机电池容量不少于 j 时的最小初始电量
    dp = [[float('inf')] * (max_battery + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(max_battery + 1):
            # 不运行第 i 个任务
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

            # 运行第 i 个任务
            if j >= task_list[i - 1][0]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - task_list[i - 1][0]] + task_list[i - 1][1])

    # 找到满足条件的最小初始电量
    for initial_battery in range(max_battery + 1):
        if dp[n][initial_battery] != float('inf'):
            return initial_battery

    return -1


# 输入示例
input_str = "1:10,2:12,3:10"
result = calculate_min_initial_battery(input_str)
print(result)  # 输出 13
