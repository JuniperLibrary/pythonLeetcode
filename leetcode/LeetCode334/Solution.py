from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        334.递增的三元子序列
        给你一个整数数组 nums ,判断这个数组中是否存在长度为 3 的递增子序列

        如果存在这样的三元组下标（i,j,k）,且满足 i<j<k,使得 nums[i] < nums[j] < nums[k],返回true；
        否则，返回false。

        输入：nums = [1,2,3,4,5]
        输出：true
        解释：任何 i < j < k 的三元组都满足题意
        """
        n = len(nums)
        if n < 3:
            return False
        # 创建一个包含 n 个元素的列表，并将每个元素初始化为 0
        left_min = [0] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])

        right_max = [0] * n
        right_max[n - 1] = nums[n - 1]
        # 这个 range 对象会生成一个从 n - 2 开始，一直递减到 -1（不包括 -1）的整数序列，步长为 -1，即每次递减 1。
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        for i in range(1, n - 1):
            if left_min[i - 1] < nums[i] < right_max[i + 1]:
                return True
        return False

    @staticmethod
    def increasing_triplet(nums) -> bool:
        # first 和 second 分别表示当前找到的递增子序列中的第一个和第二个元素
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


if __name__ == '__main__':
    print(Solution.increasing_triplet([20, 100, 10, 12, 5, 13]))
    print(Solution().increasingTriplet([20, 100, 10, 12, 5, 13]))
