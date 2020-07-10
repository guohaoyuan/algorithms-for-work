# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1 特殊情况，链表为空
        if not head:
            return head

        # 2. 初始化快慢指针
        slow, fast = head, head

        # 3. 算法流程、
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        fast = head

        while True:
            if fast == slow:
                return fast

            fast = fast.next
            slow = slow.next

            if slow == fast:
                return fast