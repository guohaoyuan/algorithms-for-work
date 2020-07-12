"""
做这个题之前，先做leetcode104

平衡二叉树要求，每个节点都是平衡的

定义一个函数求树的深度，如果左右子树的深度超过1,直接返回-1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1
            return 1 + max(left, right) if abs(left - right) < 2 else -1

        depth = helper(root)
        return depth != -1