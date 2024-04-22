class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

if __name__ == '__main__':
    s = Solution().reverseWords("Let's take LeetCode contest")
    print(s)