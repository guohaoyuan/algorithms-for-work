"""
上来就是广度优先，
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 1. 特殊情况，节点为空
        if not root:
            return []

        # 2. bfs
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            # size
            size = len(queue)
            tmp = []
            for i in range(size):
                cur = queue.popleft()
                tmp.append(cur.val)

                # 添加左右子树
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res