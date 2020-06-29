# -*- coding : utf-8 -*-

class Solution(object):

    def maxDepth(self, root):
        """

        :param root:
        :return:
        """
        # 1. 递归结束条件，越过叶子节点
        if not root:
            return 0

        # 2. 递归操作
        # 分别看左右子树的深度
        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)

        return depthLeft + 1 if depthLeft > depthRight else depthRight + 1