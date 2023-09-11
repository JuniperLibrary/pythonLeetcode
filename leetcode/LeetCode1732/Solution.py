from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        1732. 找到最高海拔
        有一个自行车手打算进行一场公路骑行，这条线路总共有n+1个不同的海拔点组成。
        自行车手从海拔为0的点开始骑行

        给你一个长度为n的数组gain，其中gain[i]是点i和点i+1的静海拔高度差（0 <= i < n ）
        请你返回最高点的海拔

        输入：gain = [-5,1,5,0,-7]
        输出：1
        解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1

        :param gain:
        :return:
        """
        # ans = total = 0
        # for i in gain:
        #     total += i
        #     ans = max(ans, total)
        # return ans
        return max(accumulate(gain, initial=0))


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    print(Solution().largestAltitude(gain))
