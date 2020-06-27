"""
在while True:里面按照正常逻辑执行就行
"""


class Solution:

    def hasCycle(self, head):

        if not head:
            return False

        slow, fast = head, head

        while True:
            # 如果遇到结尾就跳出
            if not fast or not fast.next:
                return False
            else:
                fast = fast.next.next
                slow = slow.next

            if fast == slow:
                return True