from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        """
        LCP 50 宝石补给
        每位勇者初始都拥有一些宝石 gem[i] 表示第 i 位勇者的宝石数量。
        现在这些勇者们进行了一系列的赠送，operations[j]=[x,y]
        表示在第 j 次的赠送中第 x 位勇者将自己一半的宝石（向下取整）赠送给第 y 位勇者

        在完成所有的赠送后，请找到拥有最多的宝石的勇者和拥有最少的勇者，返回二者的宝石数量之差
        """
        for x, y in operations:
            numbers = gem[x] // 2
            gem[x] -= numbers
            gem[y] += numbers
        gem_max, gem_min = gem[0], gem[0]
        for number in gem:
            gem_max = max(gem_max, number)
            gem_min = min(gem_min, number)
        return gem_max - gem_min
