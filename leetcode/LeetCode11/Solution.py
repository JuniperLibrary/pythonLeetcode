from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        11. 盛最多的水容器
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。
        说明：你不能倾斜容器。

        输入：[1,8,6,2,5,4,8,3,7]
        输出：49
        解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
        """
        ans = 0
        left = 0
        right = len(height)-1

        while left < right:
            # (right - left) 长
            #
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                # 说明此时高度太小了  想要面积最大 需要向右 移动
                left += 1
            else:
                # 说明 右边的高度太小 想要面积最大 需要向 左移动
                right -= 1
        return ans


if __name__ == '__main__':
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(heights))
