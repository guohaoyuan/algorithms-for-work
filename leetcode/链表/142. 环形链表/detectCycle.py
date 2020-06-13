# -*- coding : utf-8 -*-

class Solution(object):
    def detectedCycle(self, head):
        """
        这个不能确定链表是否有环，如果有环返回环的入口节点
        :param head:
        :return:
        """
        # 1. 特殊情况：头节点不为空或头节点的下一节点不为空
        if not head or not head.next:
            return

        # 2. 初始化快慢指针
        low, fast = head, head

        # 3. 算法流程
        # 先证明是否有环
        while True:
            if not fast or not fast.next:
                return
            fast = fast.next.next
            low = low.next
            if fast == low:
                break
        # 再找到节点
        fast = head

        while True: # 因为有可能已经在环处相遇，此时在保持同步，将永远错过彼此
            if fast == low:
                return fast
            fast = fast.next
            low = low.next
"""
时间复杂度：如果无环时间复杂度n，有环时间复杂度n也是n，是D+S1
空间复杂度：1
"""