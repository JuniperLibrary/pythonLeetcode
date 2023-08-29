from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        283.移动零
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        请注意 ，必须在不复制数组的情况下原地对数组进行操作。
        输入: nums = [0,1,0,3,12]
        [1,0,0,3,12] ->
                        [1,3,0,0,12] ->
                                        [1,3,0,0,12] ->
                                                        [1,3,0,12,0] ->
                                                                        [1,3,12,0,0]
        输出: [1,3,12,0,0]
        """
        # 初始化非0元素应该被放置的位置
        non_zero_idx = 0

        for num in nums:
            # 如果当前元素非零，将其放置到 non_zero_idx 的位置，并将 non_zero_idx 向后移动
            if num != 0:
                nums[non_zero_idx] = num
                non_zero_idx += 1
        # 将剩余的位置填充为0
        while non_zero_idx < len(nums):
            nums[non_zero_idx] = 0
            non_zero_idx += 1


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
