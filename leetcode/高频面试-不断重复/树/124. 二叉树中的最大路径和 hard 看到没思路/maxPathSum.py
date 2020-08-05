"""
定义一个函数
    1. 递归结束条件是，当前节点为空，则返回0

    2. 由于某个节点的贡献度可能为负数,我们要用max函数取值

    3. 期间，我们更新全局变量得到最大的值，注意全局变量不能设为0,应该为-2^31

    4. 返回左右贡献度最大的值+根节点的值



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