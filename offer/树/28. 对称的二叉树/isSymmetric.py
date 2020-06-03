# -*- coding : utf-8 -*-

class Solution(object):

    def isSymmetric(self, root):
        """

        :param root:
        :return:
        """

        # 1. 特殊情况树为空
        if not root:
            return True

        # 定义递归函数
        def helper(L, R):
            """
            传入两个子树判断是否对陈
            :param L:
            :param R:
            :return:
            """
            # 1. 递归结束条件：
            # 1.1 左子树和右子树均为空，表明已经越过叶子节点
            if not L and not R:
                return True

            # 1.2 左右子树有一个不为空，则表明未完全匹配
            if not L or not R:
                return False

            # 1.3 如果左右子树的节点值不同，则无法匹配
            if L.val != R.val:
                return False

            # 2. 递归操作
            # 必须L R 的左右子树都匹配才行
            return helper(L.left, R.right) and helper(L.right, R.left)

        return helper(root.left, root.right)
    """
    时间复杂度：n，遍历每一个节点
    空间复杂度：最好最坏
    """