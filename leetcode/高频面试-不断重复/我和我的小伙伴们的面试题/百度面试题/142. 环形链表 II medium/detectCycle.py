"""
我们先梳理思路：

1. 特殊情况： 如果链表为空，直接返回-1
2. 定义快慢指针，fast slow = head head
3. 首先是确定是否有环？
    3.1 快指针走两步，慢指针走一步
    3.2 两者相遇，也有环，
    3.3 快指针跑完了就没有环
    有个细节，我们要求的是再次相遇，所以判断条件放在结尾
4. 如果有环，我们要确定入环第一个节点？
    4.1 将快指针置0头节点,
    4.2 两个指针都一次走一步，看两者是否是否相遇。
    有个细节可能一开始就相遇，判断条件放在开头
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1
        if not head:
            return head

        #
        slow, fast = head, head

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
                return slow
            fast = fast.next
            slow = slow.next
