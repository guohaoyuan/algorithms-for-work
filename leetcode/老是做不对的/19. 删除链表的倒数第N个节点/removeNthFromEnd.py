"""
创建了虚拟头节点
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. 特殊情况
        if not head:
            return head
        dummy = ListNode(0)

        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next

        while True:
            if fast and not fast.next:  # if not fast.next:
                slow.next = slow.next.next
                return dummy.next
            else:
                slow = slow.next
                fast = fast.next
