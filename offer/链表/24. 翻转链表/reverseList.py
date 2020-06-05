# -*- coding : utf-8 -*-

class Solution:
    def reverseList(self, head):
        """

        :param head:
        :return:
        """
        # 1. 特殊情况：头节点为空
        if not head:
            return head

        # 2. 初始化前指针，当前指针，后指针
        pre = None
        cur = head
        nx = head.next

        # 3. 算法流程：在遍历过程中后指针指向空就是结束了
        while True:
            cur.next = pre

            if not nx:
                return cur

            pre = cur
            cur = nx
            nx = nx.next
"""
时间复杂度：n，遍历一次链表
空间复杂度：1，
"""