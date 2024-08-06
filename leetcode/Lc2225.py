from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
            没有输掉任何比赛 和 恰好输掉一场比赛的
        """
        freq = Counter()
        for winner, loser in matches:
            if winner not in freq:
                freq[winner] = 0
            freq[loser] += 1

        ans = [[], []]
        for key, value in freq.items():
            if value < 2:
                ans[value].append(key)

        ans[0].sort()
        ans[1].sort()
        return ans


if __name__ == '__main__':
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    print(Solution().findWinners(matches))
