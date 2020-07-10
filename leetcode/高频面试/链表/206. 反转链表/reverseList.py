# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # 初始化三个指针
        pre = None
        cur = head
        nt = head.next

        while True:
            if not nt:
                cur.next = pre
                return cur

            else:
                cur.next = pre
                pre = cur
                cur = nt
                nt = nt.next
