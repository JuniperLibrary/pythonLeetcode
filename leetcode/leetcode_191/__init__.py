# LeetCode 191 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 与运算
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret
