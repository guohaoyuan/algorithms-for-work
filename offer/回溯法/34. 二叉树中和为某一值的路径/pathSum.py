# -*- coding : utf-8 -*-

class Solution:

    def sumPath(self, root, sum):
        # 1. 特殊情况空树
        if not root:
            return []

        # 2. 初始化返回结果res，路径path
        res, path = [], []

        # 3. 定义递归函数
        def helper(node, tar):
            """

            :param node: 当前节点
            :param tar: 目标值
            :return: 没有返回，直接修改path res
            """
            # 3.1 结束条件：到达了叶子节点，直接返回
            if not node:
                return

            # 3.2 递归操作
            # 将当前节点加入到路径中，且更新目标值
            path.append(node.val)
            tar -= node.val

            # 更新过目标值，看是否满足条件
            # 目标值为0且已经到达叶子节点,直接返回
            if tar == 0 and not node.left and not node.right:
                res.append(list(path))

            # 递归操作左右子树
            helper(node.left, tar)
            helper(node.right, tar)

            # 撤销选择
            path.pop()

        helper(root, sum)
        return res
