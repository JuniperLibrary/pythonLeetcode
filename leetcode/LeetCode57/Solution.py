from typing import List


class Solution:
    @staticmethod
    def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        LeetCode 57.合并区间
        输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
        输出：[[1,5],[6,9]]
        """
        left, right = newInterval
        placed = False
        ans = list()
        for i, j in intervals:
            if i > right:
                if not placed:
                    ans.append([left,right])
                    placed=True
                ans.append([i,j])
            elif j < left:
                ans.append([i,j])
            else:
                left =min(left,i)
                right =max(right,j)

        if not placed:
            ans.append([left,right])

        return ans


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    insert = Solution.insert(intervals,newInterval)
    print(insert)

