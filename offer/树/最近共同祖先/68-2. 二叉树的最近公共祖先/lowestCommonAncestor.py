# -*- coding : utf-8 -*-

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        分四种情况：
        1. 根节点==其中一个值，则返回分解点
        2. 左子树为空，则在右子树
        3. 右子树为空，则在左子树
        4. 左右子树均为存在，则在根节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root:
            return

        if root.val == q.val or root.val == p.val:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if not l and r:
            return r
        if not r and l:
            return l
        if l and r:
            return root