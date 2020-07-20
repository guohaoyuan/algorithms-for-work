# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 1. 特殊情况 树为空
        if not root:
            return False

        # 创建队列
        queue = collections.deque()

        # 创建一个集合，避免走回头路
        # 但是在二叉树中不用担心

        # 将起点加图队列，也就是根节点加入
        queue.append((root, root.val))

        # 记录扩散的步数
        # step = 1

        while queue:
            size = len(queue)
            # 当前节点向四周扩散
            for i in range(size):
                cur, target = queue.popleft()

                # 判断是否到达终点，就是和是否为sum
                if not cur.left and not cur.right:
                    if target == sum:
                        # 到达叶子节点且达到目标
                        return True

                # 将周围节点加入队列
                if cur.left:
                    queue.append((cur.left, target + cur.left.val))
                if cur.right:
                    queue.append((cur.right, target + cur.right.val))
        return False


"""
递归写法：

1. 递归结束条件：
    当前节点为空，直接返回Flase
    如果当前节点为叶子节点，且和达到目标值，返回True

2. 递归操作：
    递归进入左子树 or 递归进入右子树，
    
时间复杂度：N，节点数目
空间复杂度：树的高度，最好情况是logn,最差情况是N
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            if sum - root.val == 0:
                return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)