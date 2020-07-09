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
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # 奇数
        odd = head
        oddhead = head
        # 偶数
        even = head.next
        evenhead = head.next

        while even and even.next:
            # 更改连接
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        # 连接两个断开的链表
        odd.next = evenhead
        return head