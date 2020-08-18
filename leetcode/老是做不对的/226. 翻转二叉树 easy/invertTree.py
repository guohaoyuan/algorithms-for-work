"""
思想很简单利用bfs

核心思想是：遍历节点，并两两交换

1. 特殊情况：根节点为空

2. 创建双端队列，根节点入队

3. while queue:
    size = len(queue)   # 每次遍历

    for i in range(size):
        当前节点出队 dur = queue.popleft()
        交换两个节点，要保证当前节点存在
        if cur:
            if cur.left or cur.right:
                cur.left, cur.right = cur.right, cur.left
                此时交换完了，将子树入队
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

4, 返回结果

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root



"""
递归着实很变态哦
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
"""
非递归版本
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root