"""
递归
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


"""
非递归
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre = None
        cur = head
        nt = head.next

        while nt:
            cur.next = pre
            pre = cur
            cur = nt
            nt = nt.next
        cur.next = pre
        return cur