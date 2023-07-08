from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i+1, j+1]
        return [-1, -1]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
