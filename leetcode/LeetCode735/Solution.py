from typing import List


class Solution:
    def asteroidsCollision(self, asteroids: List[int]) -> List[int]:
        """
        735.行星碰撞
        给定一个整数数组 asteroids，表示在同一行的行星。
        对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）
        每一颗行星以相同的速度移动。
        找出碰撞后剩下的所有行星。
        碰撞规则：
        两个行星相互碰撞，较小的行星会爆炸。
        如果两颗行星大小相同，则两颗行星都会爆炸。
        两颗移动方向相同的行星，永远不会发生碰撞。
        输入：asteroids = [5,10,-5]
        输出：[5,10]
        解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
        """
        stack = []
        for t in asteroids:
            boom = True
            # 栈顶元素 大于 0 并且 t 小于0
            while boom and stack and stack[-1] > 0 and t < 0:
                top = stack[-1]
                # 取绝对值
                b = -t
                if top >= b:
                    boom = False
                if top <= b:
                    # 较小的行星爆炸
                    stack.pop(-1)
            if boom:
                stack.append(t)
        return stack