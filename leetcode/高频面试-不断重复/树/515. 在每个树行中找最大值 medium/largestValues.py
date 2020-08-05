"""
bfs很开心，一把过


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            tmp = - float('inf')
            for i in range(size):
                cur = queue.popleft()

                if tmp < cur.val:
                    tmp = cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(tmp)
        return res