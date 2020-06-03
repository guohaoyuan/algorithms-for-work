# -*- coding : utf-8 -*-

class Solution:
    def kthLargest(self, root, k):
        """
        类似与leetcode 215
        :param root:
        :param k:
        :return:
        """
        # 1. 特殊情况：根节点为空
        if not root:
            return

        # 2. 初始化实例变量self.res self.k
        self.res = 0
        self.k = k

        # 3 定义递归函数
        def helper(root):
            """
            递归函数，中序遍历的逆序，且在根节点处，更新k值，self.res
            :param root:
            :return:
            """
            # 3.1 结束条件，越过叶子节点
            if not root:
                return

            # 3.2 递归操作
            helper(root.right)

            if self.k == 0:
                return  # 可以返回res，但不用，因为实例变量已经被更新
            self.k -= 1
            if self.k == 0:
                self.res = root.val

            helper(root.left)

        helper(root)
        return self.res