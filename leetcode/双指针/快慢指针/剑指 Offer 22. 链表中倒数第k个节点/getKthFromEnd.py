"""
第一反应是遍历两次链表,第一次统计长度,第二次找到目标节点
可是我们想遍历一次

所以使用快慢指针,想让fast往前走k - 1步
然后两者起步走
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head, k):
        if not head:
            return head

        slow, fast = head, head
        count = k - 1
        while count:
            fast = fast.next
            count -= 1

        while True:
            if not fast or not fast.next:
                return slow
            else:
                fast = fast.next
                slow = slow.next