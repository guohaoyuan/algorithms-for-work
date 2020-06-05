# -*- coding : utf-8 -*-

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        首先想到暴力法，外层遍历第一个链表，内层遍历第二个链表
        时间复杂度m*n，是我们不想要的
        我们需要确认是否一定有相交，
        :param headA:
        :param headB:
        :return: 返回的是相交节点
        """
        # 1. 特殊情况：其中一个链表为空直接返回，
        if not headA or not headB:
            return

        # 2. 初始化：
        node1 = headA
        node2 = headB

        # 3. 算法流程：当两节点不相等时，遍历
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1
"""
时间复杂度：m+n
空间复杂度：1
"""