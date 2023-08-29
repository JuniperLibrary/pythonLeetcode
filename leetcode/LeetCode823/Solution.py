from functools import cache
from typing import List


class Solution:

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        823.带因子的二叉树
        给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
        用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
        满足条件的二叉树一共有多少个？答案可能很大，返回 对 109 + 7 取余 的结果。
        输入: arr = [2, 4]
        输出: 3 解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
        """
        # 其中 每个非叶子节点的值应等于它的子节点的值的乘积
        # 因此，如果一个数 'x' 在数组中出现了 'k' 次，那么在构建二叉树时，我们可以把这个数分成 'k' 份，每份作为一个结点值
        # 接下来，我们可以使用dp来计算符合条件的不同二叉树的数量。对于每个结点值 'x' ,我们可以选择将其拆分为'i'份，其中 'i' 的范围为 1 到 'k'
        # 然后递归地计算左右子树可能的组合，这将构成不同的二叉树
        """
        mod = 10 ** 9 + 7
        arr.sort()
        # 用于存储每个数作为根节点时的可能的二叉树的数量
        dp = {}

        for ind, val in enumerate(arr):
            dp[val] = 1
            for j in range(ind):
                # val // arr[j] 整数除法
                if val % arr[j] == 0 and val // arr[j] in dp:
                    dp[val] += dp[arr[j]] + dp[val // arr[j]]
            dp[val] %= mod
        return sum(dp.values()) % mod
        """

        mod = 10 ** 9 + 7

        @cache
        def dfs(num):
            # 自身
            res = 1
            for i in range(len(arr)):
                if arr[i] >= num:
                    break
                #  浮点除法
                r = num / arr[i]
                if r in se:
                    # r 和 arr[i] 是 num 的子节点
                    res += dfs(r) * dfs(arr[i])
            return res

        arr = sorted(arr)
        se = set(arr)
        res = 0
        for a in arr:
            res += dfs(a)
        return res % mod


if __name__ == '__main__':

    """
    arr = [10, 20, 30, 40]
    for i, x in enumerate(arr):
        print(f"Index: {i}, Value: {x}")
    """

    arr = [2, 4]
    print(Solution().numFactoredBinaryTrees(arr))
