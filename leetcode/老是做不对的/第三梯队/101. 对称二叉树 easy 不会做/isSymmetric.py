"""
题干要求递归非递归两种做法：

1. 非递归做法就是一开始根节点进入两次

2. 在while中，size= len(queue)//2
    同时queue.popleft两次
    如果两个节点均为空：
        continue
    如果其中一个节点为空：
        return False
    接下来两个节点均存在，如果两节点的值不同，
        return False
    否则：
        当前节点1的左子树入队
        当前节点2的右子树入队
        当前节点1的右子树入队
        当前节点2的左子树入队
3. return True
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = collections.deque()
        queue.append(root)
        queue.append(root)

        while queue:
            size = len(queue) // 2
            for i in range(size):
                cur1 = queue.popleft()
                cur2 = queue.popleft()
                if not cur1 and not cur2:
                    continue

                if not cur1 or not cur2:
                    return False

                if cur1.val != cur2.val:
                    return False
                else:
                    queue.append(cur1.left)
                    queue.append(cur2.right)
                    queue.append(cur1.right)
                    queue.append(cur2.left)
        return True

"""
递归操作总觉得在哪里见到过，等我重头到位在做一遍就会了
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1 and node2:
                return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)

        res = helper(root, root)
        return res