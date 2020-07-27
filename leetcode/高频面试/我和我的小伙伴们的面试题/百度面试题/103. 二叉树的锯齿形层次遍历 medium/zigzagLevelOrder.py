"""
层序遍历，没什么好说的
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = collections.deque()
        queue.append(root)
        i = 0

        while queue:
            tmp = []
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()

                if cur:
                    tmp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if i & 1 == 0:  # 偶数行
                res.append(tmp)
            else:
                # print(tmp)
                res.append(tmp[::-1])
            i += 1
        return res