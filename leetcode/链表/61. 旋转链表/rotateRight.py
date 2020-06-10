# -*- coding : utf-8 -*-

class Solution:
    def rotateRight(self, head, k):
        """

        :param head:
        :param k: int 旋转多少位
        :return:
        """
        # 1. 特殊情况链表中只有一个节点或者没有节点
        if not head or not head.next:
            return head

        # 2. 初始化当前节点
        node = head
        n = 1

        # 3. 算法流程
        # 3.1 统计链表长度,并连接成环
        while node.next:
            n += 1
            node = node.next
        node.next = head


        # 3.2 得到k的余数
        k = k % n

        # 3.3 初始化计数器 n-k-1对应位置就停止

        new_tail = head
        for i in range(n - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None
        return new_head