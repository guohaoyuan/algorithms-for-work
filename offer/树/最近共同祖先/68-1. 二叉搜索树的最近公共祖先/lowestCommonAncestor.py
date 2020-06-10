# -*- coding : utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        二叉搜索树的共同祖先
        :param root: 根节点，
        :param p:
        :param q:
        :return: 返回节点
        """
        # # 1.
        # if not root:
        #     return

        # 2. 递归操作


        if root.val < p and root.val < q:
            return self.lowestCommonAncestor(root.right, p, q)

        elif root.val > p and root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root

    def lowestCommonAncestor_v2(self, root, p, q):
        node = root

        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
        return
