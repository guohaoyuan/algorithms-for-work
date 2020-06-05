# -*- coding : utf-8 -*-

class Solution:
    def merge(self, pHead1, pHead2):
        """

        :param pHead1:
        :param pHead2:
        :return:
        """
        # 1. 递归结束条件：其中一个链表为空，则返回另一个链表
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        # 2. 递归操作
        # 先初始化返回结果
        node = None

        # 先判断哪个是第一个头节点
        if pHead1.val <= pHead2.val:
            node = pHead1
            node.next = self.merge(pHead1.next, pHead2)
        else:
            node = pHead2
            node.next = self.merge(pHead1, pHead2.next)

        return node
"""
时间复杂度：n，一共有多少个节点
空间复杂度：1
"""