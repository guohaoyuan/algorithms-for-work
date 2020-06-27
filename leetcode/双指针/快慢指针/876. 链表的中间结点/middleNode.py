# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head) :
        if not head:
            return None

        slow, fast = head, head

        while True:
            if not fast or not fast.next:
                return slow
            else:
                fast = fast.next.next
                slow = slow.next
