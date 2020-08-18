"""
首先
    递归结束条件是当前节点为空，返回0
    递归操作是返回当前节点的能够多少个符合目标sum+左节点递+右节点递归

函数计算有多少符合目标的sum
    递归结束条件是当前节点为空，返回0
    递归操作如果当前节点不为空，则sum-=node.val
        如果sum==0，则计数器+1
    返回计数器+左节点递归+右节点递归
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.calculate(root, sum)

    def calculate(self, root, sum):
        if not root:
            return 0

        count = 0
        sum = sum - root.val
        if sum == 0:
            count += 1
        return count + self.calculate(root.left, sum) + self.calculate(root.right, sum)