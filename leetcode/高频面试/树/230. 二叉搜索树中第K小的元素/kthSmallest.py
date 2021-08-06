"""
二叉搜索树是有序的结构
一般“什么时候做的问题”是在中序遍历
“怎么做问题”是建立一个数count用来计数，如果当前位置是第k个位置，就可以返回结果了
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        # 用于计数和返回结果
        self.count = 0
        self.res = -1

    def inorder(self, root, k):
        # 特殊情况：当前节点为空
        if not root:
            return
        
        self.inorder(root.left, k)

        # 计数
        self.count += 1
        # 确认是不是第k次
        if k == self.count:
            self.res = root.val
        
        self.inorder(root.right, k)

        return

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root, k)

        return self.res
