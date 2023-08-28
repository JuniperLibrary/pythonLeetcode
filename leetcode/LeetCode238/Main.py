from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        """
        238. 除自身以外数组的乘积
        给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
        题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
        请不要使用除法，且在 O(n) 时间复杂度内完成此题。
        输入: nums = [1,2,3,4]
        输出: [24,12,8,6]
        :param nums:
        :return:
        """

        length = len(nums)
        left, right, answer = [0] * length, [0] * length, [0] * length

        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]

        right[length - 1] = 1
        for i in reversed(range(0, length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution.productExceptSelf(nums))
