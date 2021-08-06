"""
明确两个问题：
    1. 每个节点做什么
    2. 什么时候做

对于第一个问题，
    需要将比该节点大的值全部累加，包含自身也要累加
    需要我们降序打印，打印当前节点时候需要sum_node+=root.val;
    需要将当前节点的值进行替换root.val = sum_node

对于第二个问题，
    在中序遍历的中间进行
    将中序遍历整个过程翻过来
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.sum = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return
        
        # 逆序中序遍历
        self.traverse(root.right)

        # 将大于等于当前节点的全部累加
        self.sum += root.val
        # 进行节点值更新
        root.val = self.sum

        self.traverse(root.left)

        return
