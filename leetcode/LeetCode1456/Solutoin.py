class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        请返回字符串s 中长度为 k 的单个子字符串可能包含的最大元音字母数
        """

        def isVowe(ch):
            return int(ch in "aeiou")

        n = len(s)
        vowel_count = sum(1 for i in range(k) if isVowe(s[i]))
        ans = vowel_count
        for i in range(k, n):
            vowel_count += isVowe(s[i]) - isVowe(s[i - k])
            ans = max(ans, vowel_count)
        return ans


if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    Solution().maxVowels(s, k)
