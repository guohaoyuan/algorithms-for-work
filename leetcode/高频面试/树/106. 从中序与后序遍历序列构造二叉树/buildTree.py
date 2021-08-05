"""
首先，后序遍历最后一个元素是根节点；
然后，在中序遍历中找到对应的根节点并记录对应索引index
    中序遍历index左边的就是左子树；右边的就是右子树
最后，进行递归，并划分区间左子树[:index]  [:index]
                
                        右子树[index + 1:] [index: -1]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        
        # 找到根节点root_val
        root_val = postorder[-1]

        # 在中序遍历中找到对应根节点并记录索引
        index = 0
        for i, num in enumerate(inorder):
            if root_val == num:
                index = i
            
        # 进行递归
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index : -1])

        return root
