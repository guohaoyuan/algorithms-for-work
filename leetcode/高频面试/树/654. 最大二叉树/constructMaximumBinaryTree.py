"""
对于每一个根节点，只需要找到当前nums中的最大值和对应的索引，
然后递归调用左右数组构造左右子树
"""

import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        # 找到数组中的最大值及其对应索引
        max_value = - sys.maxsize
        index = 0
        for i, num in enumerate(nums):
            if num > max_value:
                max_value = num
                index = i
        
        # 创建根节点并进行递归
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root
