# -*- coding : utf-8 -*-

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        能立刻想到是，先遍历链表得到链表长度，然后在遍历链表达到n-k，显然遍历两次链表的时间复杂度是不优秀
        :param head:
        :param k:
        :return:
        """
        # 1. 特殊情况：链表head为空
        if not head:
            return

        # 2. 初始双指针former latter
        former = head
        latter = head

        for i in range(k):
            latter = latter.next

        # 3. 算法流程
        while latter:
            # 目标是latter走到最后一个节点
            former = former.next
            latter = latter.next
        return former.val