from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        输出：[1,2,2,3,5,6]
        解释：需要合并 [1,2,3] 和 [2,5,6] 。
        合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        # nums2 还有要合并的元素
        while p2 >= 0:
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # 填入 nums1[p1]
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # 填入 nums2[p1]
                nums1[p] = nums2[p2]
                p2 -= 1
            # 下一个要填入的位置
            p -= 1



if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    print(nums2)
