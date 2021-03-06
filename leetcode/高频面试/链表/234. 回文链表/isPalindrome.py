# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. 特殊情况：数组为空
        if not head:
            return True

        # 2. 初始化快慢指针
        slow = head
        fast = head

        # 3.
        while True:
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next

        # 保证fast位于后半部分
        if fast:
            slow = slow.next

        # 定义翻转函数
        def helper(head):
            # 保证数组长度为2
            if not head or not head.next:
                return head

            last = helper(head.next)
            head.next.next = head
            head.next = None
            return last

        last = helper(slow)
        p1 = head
        p2 = last
        # 后半段和前半段进行比较
        while p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        return True

"""
后半部分长短不一，我们取短的就行
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def reverse(head):
            if not head or not head.next:
                return head

            pre = None
            cur = head
            nt = head.next

            while True:
                if not nt:
                    cur.next = pre
                    return cur

                cur.next = pre
                pre = cur
                cur = nt
                nt = nt.next

        if not head or not head.next:
            return True
        slow, fast = head, head
        while True:

            if not fast or not fast.next:
                break
            fast = fast.next.next
            slow = slow.next

        last = reverse(slow)
        p1 = head
        p2 = last  # 长
        # print(p1)
        # print(p2)

        while p2:

            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True