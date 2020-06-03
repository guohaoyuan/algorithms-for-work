# -*- coding : utf-8 -*-

class Solution(object):

    def getNext(self, pNode):
        """
        心中记住那个图，分如下三种情况
        1. 该节点有右子树，
            则直接找其右子树的最左子树

        2. 该节点无右子树，且父节点存在且为父节点的左子树
            则，找到其父节点

        3. 该节点无右子树，且父节点存在且为父节点的右子树
            则，向上追溯，找到一个节点，他为自己父节点的左子树，简单理解就是找到拐点

        本方法使用迭代完成
        :param pNode:
        :return: 返回其next节点
        """

        # 1. 特殊情况树为空
        if not pNode:
            return

        # 2. 初始化当前节点
        node = pNode

        # 3. 算法流程
        # 直接分情况讨论
        # 3.1
        if node.right:
            # 如果有右子树，则进入右子树，并找到最左节点
            node = node.right
            while node.left:
                node = node.left    # 已经找到，最左节点，最后一次while
            return node

        # 3.2
        # 已将建立在没有右子树的情况下
        if node.next and node.next.left == node:
            # 找到其父节点
            return node.next

        # 3.3
        # 已经建立在没有右子树的情况下，
        if node.next and node.next.right == node:
            tmp = node.next
            while tmp.next and tmp.next.right == tmp:
                tmp = tmp.next  # 向上追溯
                # 最后一次while得到的是拐点
            return tmp.next # 返回拐点的父节点