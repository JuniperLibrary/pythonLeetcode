from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        2965. 找出缺失和重复的数字
        """
        n = len(grid)
        count = [0] * (n * n + 1)
        for row in grid:
            for x in row:
                count[x] += 1

        ans = [0, 0]
        for i in range(1, n * n + 1):
            # 出现2次的
            if count[i] == 2:
                ans[0] = i
            # 出现0次的
            if count[i] == 0:
                ans[1] = i

        return ans


if __name__ == '__main__':
    print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]))
