from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        """
        643 子数组最大平均数I
        给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
        请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
        任何误差小于 10-5 的答案都将被视为正确答案。

        输入：nums = [1,12,-5,-6,50,3], k = 4
        输出：12.75
        解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        # 连续子数组  平均数最大
        # 且长度为K
        """
        由于规定了子数组的长度为 k，因此可以通过寻找子数组的最大元素和的方式寻找子数组的最大平均数，元素和最大的子数组对应的平均数也是最大的。
        假设两个不同的子数组的长度都是 k，这两个子数组的元素和分别是 x 和 y，则这两个子数组的平均数分别是 x/k 和 y/k。
        如果 x≥y，则有 x/k≥y/k，即如果一个子数组的元素和更大，则该子数组的平均数也更大。
        """
        """
        为了找到子数组的最大元素和，需要对数组中的每个长度为 k 的子数组分别计算元素和。
        对于长度为 n 的数组，当 k≤n 时，有 n−k+1 个长度为 k 的子数组。 假设 n= 6,总共有长度为4且连续的子数组 。6-4+1=3
        如果直接计算每个子数组的元素和，则时间复杂度过高，无法通过全部测试用例，因此需要使用时间复杂度更低的方法计算每个子数组的元素和。
        """
        # nums中前k位子数组之和
        max_total = total = sum(nums[:k])
        for i in range(k, n):
            # print(i, k, n)
            # print(nums[i - k])
            # print(nums[i])
            # print(total)
            total = total - nums[i - k] + nums[i]
            max_total = max(max_total, total)
        return max_total / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    # max_total = max_sum = sum(nums[:k])
    # print(max_total, max_sum)
    Solution.findMaxAverage(nums, k)
