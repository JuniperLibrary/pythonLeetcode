import math
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        """
        LCP 06. 拿硬币
        每次最少拿 1 或 2
        求拿完所有里扣币的最少次数
        """
        times = 0
        for c in coins:
            times += math.ceil(c / 2)
        return times


if __name__ == '__main__':
    coins = [4, 2, 1]
    print(math.ceil(1/2))
    print(Solution().minCount(coins))
