"""
1. 如果根节点不存在，那肯定是false
2. 如果当前节点为叶子节点，且目标值已经为0,则返回true
3. 递归调用左右子树，且更新目标值
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            if sum - root.val == 0:
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)