from typing import List


class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        1268 搜索推荐系统
        给你一个产品数组 products 和 一个字符串 searchWord
        products 数组中产品都是一个字符串

        请你设计一个推荐系统 在依次输入单词 searchword 的每一个字母后，推荐 products 数组中前缀 与 searchWord 相同的最多三个产品
        如果前缀相同的可推荐产品超过三个 请按照字典返回最小的三个

        请你以二维列表的形式 返回输入 searchWord 每个字母后相应的推荐产品的列表

        输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
        输出：[
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
        ]
        :param products:
        :param searchWord:
        :return:
        """

        def addWord(root, word):
            cur = root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
                cur.words.append(word)
                cur.words.sort()
                if len(cur.words) > 3:
                    cur.words.pop()

        root = Trie()
        for word in products:
            addWord(root, word)
        ans = list()
        cur = root
        flag = False
        for ch in searchWord:
            if flag or ch not in cur.child:
                ans.append(list())
                flag = True
            else:
                cur = cur.child[ch]
                ans.append(cur.words)
        return ans


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "use"
    suggested_products = Solution().suggestedProducts(products, searchWord)
    for an in suggested_products:
        print(an)