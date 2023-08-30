from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        有一只跳蚤的家在数轴上的位置 'x' 处。请你帮助它从位置 0 出发，到达它的家
        跳蚤的跳跃规则:
        1. 它可以 往前 跳恰好 a 个位置（即往右跳）。
        2. 它可以 往后 跳恰好 b 个位置（即往左跳）。
        3. 它不能 连续 往后跳 2 次。
        4. 它不能跳到任何 forbidden 数组中的位置。
        跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
        给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，
        请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。

        输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
        输出：3
        解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
        """
        q, visited = deque([[0, 1, 0]]), set([0])
        lower, upper = 0, max(max(forbidden) + a, x) + b
        forbiddenSet = set(forbidden)
        while q:
            position, direction, step = q.popleft()
            if position == x:
                return step
            nextPosition = position + a
            nextDirection = 1
            if lower <= nextPosition <= upper and nextPosition * nextDirection not in visited and nextPosition not in forbiddenSet:
                visited.add(nextPosition * nextDirection)
                q.append([nextPosition, nextDirection, step + 1])
            if direction == 1:
                nextPosition = position - b
                nextDirection = -1
                if lower <= nextPosition <= upper and nextPosition * nextDirection not in visited and nextPosition not in forbiddenSet:
                    visited.add(nextPosition * nextDirection)
                    q.append([nextPosition, nextDirection, step + 1])
        return -1
