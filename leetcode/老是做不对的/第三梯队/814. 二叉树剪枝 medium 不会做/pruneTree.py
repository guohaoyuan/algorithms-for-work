"""
定义一个函数，判断当前节点的左右子树是否含有1.
    如果当前节点为空，直接返回F
    得到左右子树的返回结果
    如果左子树不含有1,将该节点的左子树置none
    如果右子树不含有1,将该节点的右子树置none
    返回 当前节点==1 or 左子树为T or 右子树为T
    ## 表达的意思就算当前节点不是1,只要左右子树有一个是1的就没问题，不用被减枝

主函数调用helper(root) 如果它为T, 返回root;否则返回None
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def helper(root):
            if not root:
                return False

            l = helper(root.left)
            r = helper(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None

            return root.val == 1 or l or r

        return root if helper(root) else None