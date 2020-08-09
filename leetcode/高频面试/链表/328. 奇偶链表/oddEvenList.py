"""
1. 创建四个指针，odd奇数指针，奇数头节点oddhead;even偶数指针，偶数头节点evenhead
2.  odd.next = even.next
    odd = even.next
    even.next = odd.next
    even = odd.next
3. 将奇数指针连到偶数头部

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#
#         # 奇数
#         odd = head
#         oddhead = head
#         # 偶数
#         even = head.next
#         evenhead = head.next
#
#         while even and even.next:
#             # 更改连接
#             odd.next = even.next
#             odd = even.next
#             even.next = odd.next
#             even = odd.next
#
#         # 连接两个断开的链表
#         odd.next = evenhead
#         return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 1. 特殊情况：链表长度不足2
        if not head or not head.next:
            return head

        # 2. 初始化五个指针odd, oddhead, even, evenhead, cur
        odd, oddhead = head, head
        even, evenhead = head.next, head.next

        # 3. 算法流程先连接奇偶链表
        while True:
            if not odd.next or not even.next:
                odd.next = evenhead
                even.next = None
                return oddhead
            if even.next:
                odd.next = even.next
                odd = even.next
            if odd.next:
                even.next = odd.next
                even = odd.next

"""
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        index = 3  # 第一个节点
        odd = head
        even = head.next
        p1, p2 = odd, even
        p3 = even.next
        while True:
            cur = p3
            if not cur:
                p1.next = even
                p2.next = None
                return odd
            if index & 1 == 1:  # odd
                p1.next = cur
                p1 = p1.next
                index += 1

            else:
                p2.next = cur
                p2 = p2.next
                index += 1
            p3 = p3.next