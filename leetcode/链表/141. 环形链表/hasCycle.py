# -*- coding : utf-8 -*-

class Solution:
    def hasCycle(self, head):
        """
        这个不能确定链表是否有环，如果有环返回T
        :param head:
        :return:
        """
        # 1. 特殊情况
        if not head or not head.next:
            return False

        # 2. 初始化双指针
        low, fast = head, head

        # 3, 算法流程
        while True:
            if not fast or not fast.next:
                return False
            low = low.next
            fast = fast.next.next

            if low == fast:
                return True
"""
时间复杂度：n，无环是n，有环，会在环里走k步，n+k，依旧是n
空间复杂度：1
"""