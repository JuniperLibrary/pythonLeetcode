from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = nums[0], 0
        for i in range(1, len(nums)):
            even, odd = max(even, odd + nums[i]), max(even, odd - nums[i])
        return even


if __name__ == '__main__':
    print(Solution().maxAlternatingSum([4, 2, 5, 3]))
