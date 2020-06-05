# -*- coding : utf-8 -*-

class Solution:
    def entryNodeOfLoop(self, pHead):
        """
        确定有环，返回环的入口节点
        :param pHead:
        :return:
        """
        # 1. 特殊情况:头节点为空或者头节点的下一个节点为空，因为链表长度为1无法成环
        if not pHead or not pHead.next:
            return

        # 2. 初始化快慢指针
        low, fast = pHead, pHead

        # 3. 算法流程：先让两指针在环中相遇
        # 因为一开始快慢指针本来就一样，不能上来就判断是否相等
        while True:
            low = low.next
            fast = fast.next.next
            if low == fast:
                break

        fast = pHead

        # 一种特殊情况，1->2->1此时入口是1,如果按照如下写法就是2
        # while True:
        #     low = low.next
        #     fast = fast.next
        #     if low == fast:
        #         break
        while True:
            if low == fast:
                break
            low = low.next
            fast = fast.next
        return fast
""""
时间复杂度：
空间复杂度：
"""