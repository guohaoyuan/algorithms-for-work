'''
特殊情况是：如果根节点为空，则返回空
递归中止条件：如果当前节点==p或者q，则直接返回当前节点
递归操作：进入右子树;进入左子树
如果左子树中存在并且右子树中存在，则返回根节点
如果左子树存在则返回右子树
如果右子树存在则返回左子树
如果左右子树都不存在则直接返回
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

        if root.val == p.val or root.val == q.val:  ### 重点关注
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        if left and right:
            return root
        if not left and not right:
            return