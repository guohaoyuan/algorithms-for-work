# -*- coding : utf-8 -*-

class Solution:
    def verifyPostOrder(self, postorder):
        """

        :param postorder:
        :return:
        """
        # 1. 特殊情况：列表为空则返回真
        if not postorder:
            return True



        # 3. 递归函数
        def helper(post):
            """
            分段传入
            :param post:
            :return:
            """
            # 初始化根节点
            root = post[-1]
            # 2. 初始化列表长度
            n = len(post)
            # 1. 递归结束条件
            # 1.1 先找到右子树的第一个节点
            for i in range(n):
                if post[i] > root:  # 找到右子树的第一个节点
                    break

            # 1.2 遍历右子树看其中是否存在小于根节点的值
            for j in range(i, n):   # 由于数组中无重复数字
                if post[j] < root:
                    return False

            # 2. 递归操作
            # 2.1 左子树为空则为真
            left = True
            if i > 0:
                left = helper(post[:i])

            # 2.2 右子树为空则为真
            right = True
            if i < n - 1:
                right = helper(post[i: -1])
            return left and right
        return helper(postorder)