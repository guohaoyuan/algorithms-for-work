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

"""
计算出从一个节点出发的方法数。
然后遍历整个树，计算每个节点的方法数，相加
爸爸我太牛比了，我自创新作法，哈哈哈
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = [0]

        def countMethod(root, sum):
            if not root:
                return 0
            count = 0
            if sum - root.val == 0:
                count += 1
            return count + countMethod(root.left, sum - root.val) + countMethod(root.right, sum - root.val)

        def helper(root, sum):
            if not root:
                return
            helper(root.left, sum)
            res[0] = res[0] + countMethod(root, sum)
            helper(root.right, sum)

        if not root:
            return 0

        helper(root, sum)
        return res[0]
