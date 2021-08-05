# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None

        def helper(root):
            if not root:
                return
            if not self.pre:
                self.pre = root
            else:
                self.pre.right = root
                self.pre.left = None
                self.pre = root

            # 因为在helper(root.left)中会修改root.right的指向，
            # 所以暂存right
            right = root.right
            helper(root.left)
            helper(right)

        helper(root)

"""
类似leetcode114
"""

"""
给flatten函数输入节点root，那么以root为根的二叉树就会被拉平为一条链表

怎么做：
    1. 将root的左右子树拉平
    2. 将root的左子树接到右子树下方，然后将原始右子树接到当前右子树末端

什么时候做：
    后序遍历
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        # 此时左右子树已经拉平
        left = root.left
        right = root.right

        # 将root左子树接到右子树,左子树悬空
        root.right = left
        root.left = None

        p = root
        while p.right:
            p = p.right
                
        # 将原始右子树作为当前右子树末端
        p.right = right
        
        return
