from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1

    def helper(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
