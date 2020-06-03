# -*- coding : utf-8 -*-

class Solution(object):
    def mirrorTree(self, root):
        """

        :param root:
        :return:
        """
        # 1. 递归结束条件
        if not root:
            return  # 表明越过叶子节点

        # 2. 递归操作
        # 先建立临时变量缓存左子树
        tmp = root.left

        # 递归开始
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root
    """
    时间复杂度：N，遍历了每一个节点
    空间复杂度：N,最差情况下退化为N,变为列表，最好情况logn
    """