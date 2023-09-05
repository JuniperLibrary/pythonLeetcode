from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        """
        2605 从两个数字数组里生成最小的数字

        给你两个只包含1～9之间的数字的数组 nums1 和 nums2 ，每个数组中的元素互不相同
        请你返回最小的数字都至少包含这个数字的某个数位

        nums1 = [4,1,3]
        nums2 = [5,7]
        return 1 5 -> 15
        :param nums1:
        :param nums2:
        :return:
        """

        def same() -> int:
            s = set(nums1) & set(nums2)
            return -1 if not s else min(s)

        if (x := same()) != -1:
            return x

        x = min(nums1)
        y = min(nums2)
        return min(x * 10 + y, y * 10 + x)


if __name__ == '__main__':
    nums1 = [3,5,2,6]
    nums2 = [3,1,7]
    Solution().minNumber(nums1, nums2)
