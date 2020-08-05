"""
bfs是真的猛

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if i == size - 1:
                    res.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res