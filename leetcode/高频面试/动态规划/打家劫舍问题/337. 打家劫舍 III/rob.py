"""
定义状态：dp[0]表示不偷当前节点，dp[1]表示偷当前节点

状态转移方程：
        不偷当前节点 = 偷左子树 + 偷右子树
        偷当前节点 = 不偷左子树 + 不偷右子树


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def dp(root):
            """
            本函数返回两个值组成的元组，偷当前节点，不偷当前节点得到的财产
            首先考虑递归的结束条件，当前节点为空直接返回0,0

            递归操作，首先得到左右两个子树的偷与不偷的元组
                    偷当前节点，则不偷两个子树
                    不偷当前节点，则当前节点值+偷左右子树所能获得的最大财产
            返回偷与不偷所得财产的元组

            """
            if not root:
                return 0, 0

            left = dp(root.left)
            right = dp(root.right)

            rob_y = root.val + left[1] + right[1]

            rob_n = max(left[0], left[1]) + max(right[0], right[1])

            return rob_y, rob_n

        if not root:
            return 0

        return max(dp(root))