from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        1222 可以攻击国王的皇后
        在一个 8*8 的棋盘上，放置着若干 {黑皇后} 和 {白国王}

        给定一个由整数坐标组成的数组 queens 表示黑皇后的位置
        以及一对坐标 king 表示白国王的位置
        返回所有可以攻击国王的皇后的坐标（任意顺序）

        同一行 可以攻击
        同一列 可以攻击
        对角线 可以攻击
        如果在对角线的左或右 有皇后 也不能攻击


        输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
        输出：[[0,1],[1,0],[3,3]]
        解释：
        [0,1] 的皇后可以攻击到国王，因为他们在同一行上。
        [1,0] 的皇后可以攻击到国王，因为他们在同一列上。
        [3,3] 的皇后可以攻击到国王，因为他们在同一条对角线上。
        [0,4] 的皇后无法攻击到国王，因为她被位于 [0,1] 的皇后挡住了。
        [4,0] 的皇后无法攻击到国王，因为她被位于 [1,0] 的皇后挡住了。
        [2,4] 的皇后无法攻击到国王，因为她和国王不在同一行/列/对角线上。
        """
        queen_pos = set((x, y) for x, y in queens)
        ans = list()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
            kx, ky = king[0] + dx, king[1] + dy
            while 0 <= kx < 8 and 0 <= ky < 8:
                if (kx, ky) in queen_pos:
                    ans.append([kx, ky])
                    break
                kx += dx
                ky += dy

        return ans


if __name__ == '__main__':
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    for x in Solution().queensAttacktheKing(queens, king):
        print(x)
