"""
注意：题目要求先序数组中均不重复

首先，先序第一个位置就是根节点；
然后，在中序遍历中找到根节点num以及其对应索引index。
    那么左边的就是左子树；右边的就是右子树
最后，利用后续进行递归
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        # 找到根节点
        root_val = preorder[0]
        root_index = 0

        for i, num in enumerate(inorder):
            if num == root_val:
                root_index = i
        
        # 创建根节点
        root = TreeNode(root_val)

        # 利用后续进行递归
        root.left = self.buildTree(preorder[1: 1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

        return root
