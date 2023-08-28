import collections


class Solution:

    @staticmethod
    def reverseWords(s: str) -> str:
        """
        LeetCode 151.反转字符串中单词
        给你一个字符串 s ，请你反转字符串中 单词 的顺序。
        单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
        返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
        注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
        输入：s = "the sky is blue"
        输出："blue is sky the"
        :param s:
        :return:
        """

        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []

        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        d.appendleft(''.join(word))
        return ' '.join(d)


if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution.reverseWords(s))
