"""
给定一个链表判断是否有环

快慢指针
如果两者在环内相遇,则返回True
如果两者没有在环里相遇,则返回False
"""


class Solution:
    def hasCycle(self, head):

        # 1. 特殊情况: 头节点为空, 返回False
        if not head:
            return False

        # 2. 初始化快慢指针
        slow, fast = head, head

        # 3. 算法流程找环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False