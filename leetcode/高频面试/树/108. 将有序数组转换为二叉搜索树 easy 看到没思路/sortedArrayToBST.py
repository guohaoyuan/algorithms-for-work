"""
选取中间节点为根节点

递归结束条件：左指针越过右指针 ********

递归操作：
    1. 求得中间节点索引
    2. 创建根节点，递归左子树，递归右子树
    3. 返回根节点
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        if not nums:
            return None

        return helper(0, len(nums) - 1)