# -*- coding : utf-8 -*-

class Solution(object):
    def isSubStructure(self, A, B):
        """
        递归
        :param A:
        :param B:
        :return:
        """
        # 1. 递归结束条件：A or B 为空
        if not A or not B:
            return False

        # 定义helper函数
        def helper(A, B):
            """
            用于判断在当节点相同时，是否整个树结构一致
            :param A:
            :param B:
            :return:
            """
            # 1. 结束条件有三种，
            # 1.1 树A为空表明，遍历整个A树没找到结果
            if not A:
                return False

            # 1.2 树B为空表明，遍历过程将树B匹配
            if not B:
                return True

            # 1.3 当前两个节点不一样
            if A.val != B.val:
                return False

            # 2. 递归操作:必须左右子树都匹配上
            return helper(A.left, B.left) and helper(A.right, B.right)




        # 初始化返回结果
        res = False
        # 2. 递归操作
        # 先看两个根节点是否一样
        if A.val == B.val:
            # 进入第二个递归函数helper
            res = helper(A, B)
        # 如果两个根节点不相等，则进入子树进行判断
        if not res: # 如果根节点不是答案，则A进入左子树
            res = self.isSubStructure(A.left, B)

        if not res: # 如果左子树不是答案，则A进入右子树
            res = self.isSubStructure(A.right, B)
        return res

"""
时间复杂度为：mn，最糟糕情况需要遍历两个树的所有节点
空间复杂度：m,当A退化为链表，递归深度就是m
"""