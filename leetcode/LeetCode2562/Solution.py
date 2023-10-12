from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if i != j:
                ans += int(str(nums[i]) + str(nums[j]))
            else:
                ans += nums[j]
            i += 1
            j -= 1
        return ans


nums = [5, 14, 13, 8, 12]
print(Solution().findTheArrayConcVal(nums))
