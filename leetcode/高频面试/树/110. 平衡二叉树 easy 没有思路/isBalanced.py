"""
做这个题之前，先做leetcode104

平衡二叉树要求，每个节点都是平衡的

步骤：
    1. 如果空树，直接返回0
    2. 返回左子树的深度，如果不是平衡树，返回-1
    3. 返回右子树的深度，如果不是平衡树，返回-1
    4. 返回当前节点的深度， 如果是平衡树；否则返回-1，表示不是平衡树
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1
            return 1 + max(left, right) if abs(left - right) < 2 else -1

        depth = helper(root)
        return depth != -1

"""
凡人的做法
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            return max(l, r) + 1
        res = []
        if not root:
            return True
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)
        inorder(root)
        for node in res:
            if node:
                l = helper(node.left)
                r = helper(node.right)
                tmp = True if abs(l-r) <= 1 else False
                if tmp is False:
                    return False
        return True