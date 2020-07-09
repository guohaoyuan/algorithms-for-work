"""
递归结束条件：
    如果其中一个数组为空，直接返回另一个数组

递归操作：
    如果l1.val < l2.val，则l1.next = (l1.next, l2)
    返回l1
    否则                   l2.next = (l1, l2.next)
    返回l2
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
