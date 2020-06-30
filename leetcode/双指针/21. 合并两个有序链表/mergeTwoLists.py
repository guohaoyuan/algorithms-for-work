"""
利用递归实现合并两个链表
如果l1.val <= l2.val, 就以l1为头节点,连接两个链表
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            node = l1
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = l2
            node.next = self.mergeTwoLists(l1, l2.next)
        return node