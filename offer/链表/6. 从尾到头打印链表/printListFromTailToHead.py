# -*- coding : utf-8 -*-

class Solution(object):
    def printListFromTailToHead(self, listNode):
        """
        我们使用一个栈，从头到尾存储节点
        再将队列逆序
        :param listNode:
        :return:
        """
        # 1. 特殊情况：链表为空，则返回空
        if not listNode:
            return []

        # 2. 初始化栈stack
        stack = []

        # 3. 从头到位遍历节点
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next

        # 4. 逆序
        return stack[::-1]
"""
时间复杂度：n，遍历一次链表，逆序一次栈
空间复杂度：n，使用栈
"""