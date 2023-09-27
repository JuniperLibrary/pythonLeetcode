from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """
        2603 收集树中金币
        给你一个为 n 个节点的五向无根树，节点编号从 0 到 n-1
        给你整数 n 和一个长度为 n-1 的二维数组 edges ，其中 edges[i] = [a,b]
        表示树中节点 a 和 b 之间有一条边
        再给你一个长度为 n 的数组 coins 其中coins[i] 可能为 0 也可能为 1
        1 表示节点 i 处有一个金币

        一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次
        - 收集距离当前节点距离为 2 以内的所有金币 或者
        - 移动到树中一个相临节点

        你需要收集树种所有的金币，并且返回到出发节点，请你返回最少经过的边数
        如果你多次经过一条边，每一次经过都会给答案加一
        """
