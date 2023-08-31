import collections
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        1679. K 和数对的最大数目
        给你一个整数数组 nums 和一个整数 k 。
        每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
        返回你可以对数组执行的最大操作数。

        输入：nums = [1,2,3,4], k = 5
        输出：2
        解释：开始时 nums = [1,2,3,4]：
        - 移出 1 和 4 ，之后 nums = [2,3]
        - 移出 2 和 3 ，之后 nums = []
        不再有和为 5 的数对，因此最多执行 2 次操作。

        :param nums:
        :param k:
        :return:
        """
        tmp = collections.Counter(nums)
        ans = 0
        for num in tmp:
            if num * 2 < k:
                ans += min(tmp[num], tmp.get(k - num, 0))
            elif num * 2 == k:
                ans += tmp[num] // 2
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # counter = collections.Counter(nums)
    # print(counter.get(2, 0))
    # print(counter)
    print(Solution().maxOperations(nums=nums, k=5))