"""
1. 二叉搜索数，都是已经排好序的结构，我们很自然利用中序遍历，得到一个有序数组

2. 老办法
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []

        def helper(root, res):
            if not root:
                return res

            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
            return res

        res = helper(root, res)
        if len(res) < 2:
            return False
        L, R = 0, len(res) - 1

        while L < R:
            if res[L] + res[R] == k:
                return True
            elif res[L] + res[R] > k:
                R -= 1
            elif res[L] + res[R] < k:
                L += 1
        return False
