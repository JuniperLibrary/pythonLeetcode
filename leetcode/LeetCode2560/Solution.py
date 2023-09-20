from bisect import bisect_left
from typing import List


class Solution:
    """
        不会偷取 相领 的房屋
        只会偷取 房屋中的最大的金额

        nums[i] 表示每间房屋存放的现金金额
        k 表示 偷去 最少的房屋次数 小偷总能窃取至少 k 间房屋

        返回小偷最小的偷取能力
        偷取能力 定义为 在他窃取过程中能从单间房屋中窃取的最大金额

        nums = [2,3,5,9]
        k = 2
        小偷至少偷取 2 次
        """

    def minCapability(self, nums: List[int], k: int) -> int:
        def solve(mx: int) -> int:
            """
            solve(mx) 返回最大金额为 mx 时 最多可以偷多少间房子
            :param mx:
            :return:
            """
            f0 = f1 = 0
            for x in nums:
                if x > mx:
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1

        return bisect_left(range(max(nums)), k, key=solve)


sorted_list = [10, 20, 30, 40, 50]
