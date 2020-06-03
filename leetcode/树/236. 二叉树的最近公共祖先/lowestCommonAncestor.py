# -*- coding : utf-8 -*-

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 1. 递归结束条件：越过叶子节点，直接返回
        if not root:
            return

        # 2. 递归操作：
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # 分三种情况
        if root.val == p.val or root.val == q.val:
            return root
        if l and r:
            return root

        if l and not r:
            return l
        if r and not l:
            return r