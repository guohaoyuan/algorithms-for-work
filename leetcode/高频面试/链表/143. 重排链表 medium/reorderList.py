"""
思路很简单，首先快慢指针，将链表分成前后两端
然后翻转后一段
然后连接两端
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow, fast = head, head

        while True:
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next

        # 如果是奇数个，我们将slow后移一位
        new_head = slow.next
        if not new_head:
            # 比如1->2
            return head
        # 断开，使得前一段比后一段长
        slow.next = None

        def reverse(head):
            if not head or not head.next:
                return head

            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last

        last = reverse(new_head)
        p1, p2 = head, last

        # p1长度绝对大于1
        p1_next = p1.next  # 一开始不为none
        p2_next = p2.next  # 可能为none

        while p1:

            p1.next = p2
            p2.next = p1_next

            # 更新两个指针
            p1 = p1_next
            p2 = p2_next
            # 因为p1最长，所以不用担心p1_next会不存在，灾难始终慢我一步
            p1_next = p1.next
            if not p2:
                return head
            else:
                p2_next = p2.next