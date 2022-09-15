from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        begin, end = 0, 0
        while True:
            next_max_end = end
            for i in range(begin, min(end + 1, len(nums))):
                next_max_end = max(next_max_end, nums[i])
            if next_max_end == end:
                break
            begin, end = end + 1, next_max_end
        return end >= len(nums) - 1