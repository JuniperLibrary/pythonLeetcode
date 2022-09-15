class Solution:
    def getBinaryTrees(self, preOrder: List[int], inOrder: List[int]) -> List[TreeNode]:
        def recur(root, left, right):
            if left > right: return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic, preorder = {}, preOrder
        for i in range(len(inOrder)):
            dic[inOrder[i]] = i
        return recur(0, 0, len(inOrder) - 1)
