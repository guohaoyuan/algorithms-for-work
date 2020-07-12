"""

前序遍历 preorder = [3,  9,  20,15,7]
                 左子树[1:i+1)，长度i; 右子树[i+1:]
中序遍历 inorder = [9,  3,  15,20,7]
                左子树[0: i)，长度i; 右子树[i+1:]
先序遍历的第一个值为根节点
在中序遍历中找到根节点i
然后递归先序遍历传入
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 特殊情况
        if not preorder:
            return None

        # 初始化根节点
        root = TreeNode(preorder[0])

        # 算法流程，在中序遍历中找到根节点
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root.left = self.buildTree(preorder[1:i + 1], inorder[0:i])
                root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
                # break   ### 备忘
        return root