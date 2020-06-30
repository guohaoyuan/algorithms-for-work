"""
第一反应是遍历两次链表,第一次统计长度,第二次找到目标节点
可是我们想遍历一次

所以使用快慢指针,想让fast往前走k - 1步
然后两者起步走

结束条件, 快指针到了tail
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        slow = head
        fast = head

        for i in range(k - 1):
            fast = fast.next

        while True:
            if fast and not fast.next:
                return slow
            fast = fast.next
            slow = slow.next