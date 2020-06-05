# -*- coding : utf-8 -*-
class Solution:
    def treeToDoublyList(self, root):
        """

        :param root:
        :return: 是一个链表
        """
        # 1. 特殊情况：节点为空
        if not root:
            return root

        # 2. 初始化前指针和头节点
        self.pre = None
        self.head = None

        # 3. 算法流程，在中序遍历中构造双向链表
        def inoder(cur):
            # 1. 递归结束条件，越过叶子节点
            if not cur:
                return

            # 2. 递归操作
            # 先递归左子树
            inoder(cur.left)

            # 父节点操作，建立双向链表
            # 如果当前节点的pre为空，表明为整棵树的根节点
            if not self.pre:
                self.head = cur
            else:   # 不为空表示，为中间节点
                self.pre.right = cur
                cur.left = self.pre
            # 更新pre节点
            self.pre = cur

            # 递归右子树
            inoder(cur.right)

        inoder(root)

        # 连接首尾节点
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head