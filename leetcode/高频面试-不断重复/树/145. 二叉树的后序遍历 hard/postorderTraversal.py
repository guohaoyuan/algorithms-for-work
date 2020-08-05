# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def helper(root):
            if not root:
                return root

            helper(root.left)
            helper(root.right)
            res.append(root.val)

        if not root:
            return []

        res = []

        helper(root)

        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

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
                stack.append((cur, 'g'))
                if cur.right:
                    stack.append((cur.right, 'w'))
                if cur.left:
                    stack.append((cur.left, 'w'))
        return res