"""
递归
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        def helper(root):
            if not root:
                return

            res.append(root.val)
            helper(root.left)
            helper(root.right)

        if not root:
            return []

        res = []
        helper(root)
        return res


"""
非递归对于树装结构，是要反序
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        stack.append((root, 'w'))
        res = []

        while stack:
            cur, color = stack.pop()

            if color == 'g':
                res.append(cur.val)
            else:

                if cur.right:
                    stack.append((cur.right, 'w'))
                if cur.left:
                    stack.append((cur.left, 'w'))
                stack.append((cur, 'g'))

        return res