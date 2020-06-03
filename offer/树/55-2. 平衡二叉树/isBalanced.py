# -*- coding : utf-8 -*-

class Solution:
    def isBalanced(self, root):
        """

        :param root:
        :return: boolean
        """
        def helper(root):
            # 1. 递归结束条件：
            if not root:
                return 0

            # 2. 递归操作
            left = helper(root.left)
            right = helper(root.right)
            # 2.1减枝操作
            if left == -1:
                return -1   # 表明左子树不是平衡的
            if right == -1:
                return -1   # 表明右子树不是平衡的

            # 2.2 后序遍历对根节点的操作; 左右子树的差值小于1,表明平衡；否则不平衡
            return max(left, right) + 1 if abs(left - right) <= 1 else -1


        return helper(root) != -1