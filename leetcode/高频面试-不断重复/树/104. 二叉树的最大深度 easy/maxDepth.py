"""
递归操作，类似leetcode 543 求直径
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)

            return max(r, l) + 1

        if not root:
            return 0

        return helper(root)


"""
非递归操作
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque()
        queue.append((root, 1))

        while queue:
            size = len(queue)

            for i in range(size):
                cur, depth = queue.popleft()

                if cur.left:
                    queue.append((cur.left, depth + 1))
                if cur.right:
                    queue.append((cur.right, depth + 1))
        return depth