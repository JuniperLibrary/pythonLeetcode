from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        2215 找出两数组的不同

        给你两个下标从 0 开始的整数数组 nums1 和 nums2 请你返回 一个长度为 2 的列表 answer

        answer[0] 是 nums1 中所有不存在于 nums2 中的 不同整数组成的列表
        answer[1] 是 nums2 中所有不存在于 nums1 中的不同整数组成的列表

        列表中的整数可以按任意顺序返回
        输入: nums1 = [1,2,3] nums2 = [2,4,6]
        输出: [[1,3],[4,6]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        res = [[], []]
        for num in set1:
            if num not in set2:
                res[0].append(num)
        for num in set2:
            if num not in set1:
                res[1].append(num)
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(Solution().findDifference(nums1, nums2))
