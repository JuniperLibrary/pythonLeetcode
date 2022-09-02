from typing import List


# 剑指 Offer 06. 从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

    def helper(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
