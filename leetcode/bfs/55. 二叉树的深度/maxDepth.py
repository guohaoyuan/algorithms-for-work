# -*- coding : utf-8 -*-

class Solution(object):

    def maxDepth(self, root):
        """

        :param root:
        :return:
        """
        # 1. 递归结束条件，越过叶子节点
        if not root:
            return 0

        # 2. 递归操作
        # 分别看左右子树的深度
        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)

        return depthLeft + 1 if depthLeft > depthRight else depthRight + 1

"""
非递归操作

"""
import collections


class Solution1:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        depth = 0

        while queue:
            # print(queue)
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            depth += 1
        return depth