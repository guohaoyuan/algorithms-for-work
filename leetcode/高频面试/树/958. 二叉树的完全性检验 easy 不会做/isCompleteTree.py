# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = collections.deque()
        queue.append((root, 1))
        count = 0  # 统计节点个数

        while queue:
            size = len(queue)
            for i in range(size):
                cur, position = queue.popleft()
                count += 1
                print(count, position)
                if cur.left:
                    queue.append((cur.left, position * 2))
                if cur.right:
                    queue.append((cur.right, position * 2 + 1))

        return True if position == count else False