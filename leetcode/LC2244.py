from collections import Counter
from typing import List


# 2244. 完成所有任务需要的最少轮数
class Solution:

    def minimumRounds(self, tasks: List[int]) -> int:
        """
            给你一个下标从 0 开始的整数数组 tasks ，其中 tasks[i] 表示任务的难度级别。
            在每一轮中，你可以完成 2 个或者 3 个 相同难度级别 的任务。
            返回完成所有任务需要的 最少 轮数，如果无法完成所有任务，返回 -1 。
        """
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())


if __name__ == '__main__':
    print(Solution().minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
