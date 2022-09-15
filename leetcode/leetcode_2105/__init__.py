from typing import List


# leetcode 2105.给植物浇水II
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res = 0
        n = len(plants)
        # A，B开始灌水的位置
        pos_a, pos_b = 0, n - 1
        # A，B的剩余水壶的容量
        left_a, left_b = capacityA, capacityB

        while pos_a < pos_b:
            if left_a < plants[pos_a]:
                res += 1
                left_a = capacityA - plants[pos_a]
            else:
                left_a -= plants[pos_a]
            pos_a += 1
            if left_b < plants[pos_b]:
                res += 1
                left_b = capacityB - plants[pos_b]
            else:
                left_b -= plants[pos_b]
            pos_b -= 1

        # 模拟相遇后可能得浇水的过程
        if pos_a == pos_b:
            if left_a >= left_b and left_a < plants[pos_a]:
                res += 1
            elif left_a < left_b and left_b < plants[pos_b]:
                res += 1
        return res
