"""
利用递归，
    递归结束条件：当前节点为空，返回贡献0

    递归操作：左子树的最大贡献
            右子树的最大贡献，
            更新三点的贡献
            返回当前节点的最大贡献

主方法调用递归函数，
返回三点贡献

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 1. 特殊情况：根节点为空
        if not root:
            return 0

        # 2. 初始化最大路径和
        self.max_ = - float('inf')

        # 3. 定义函数
        def helper(root):
            # 递归结束条件：当前节点为空
            if not root:
                return 0

            # 递归操作，计算左右子树的贡献度
            leftmax = max(helper(root.left), 0)
            rightmax = max(helper(root.right), 0)

            # 计算当前节点的贡献度
            self.max_ = max(self.max_, root.val + leftmax + rightmax)

            # 返回根节点的总贡献
            return root.val + max(leftmax, rightmax)

        helper(root)
        return self.max_