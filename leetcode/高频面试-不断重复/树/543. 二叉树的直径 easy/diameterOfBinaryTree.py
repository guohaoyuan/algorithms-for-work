"""
根求树的深度很相似，leetcode 55

递归写法

不能直接原封不动用55中的递归函数，因为根节点可能没有右孩子，而最长直径在左子树中
所以在递归过程更新最大长度
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            if l + r > max_depth[0]:
                max_depth[0] = l + r
            return max(l, r) + 1

        if not root:
            return 0
        max_depth = [0]

        helper(root)
        return max_depth[0]