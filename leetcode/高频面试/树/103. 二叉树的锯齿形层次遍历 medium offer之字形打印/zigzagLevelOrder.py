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

        queue = collections.deque()
        queue.append(root)
        res = []
        count = 0  # 计数器，表示当前奇数行还是偶数行

        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if count & 1:  # 奇数行
                tmp = tmp[::-1]
            else:
                tmp = tmp
            count += 1
            res.append(tmp)
        return res