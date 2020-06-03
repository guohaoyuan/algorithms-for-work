# -*- coding : utf-8 -*-
import collections

class Solution(object):

    def levelOrder(self, root):
        """
        没有使用递归，利用迭代实现
        :param root:
        :return:
        """
        # 1. 特殊情况：根节点为空
        if not root:
            return []

        # 2. 初始变量，返回结果用列表，暂存节点用双端队列
        res = []
        queue = collections.deque()
        queue.append(root)

        # 3. 算法流程
        while queue:
            # 出队
            node = queue.popleft()
            # 将当前节点加入返回结果中
            res.append(node.val)
            # 将当前节点的左右子节点加入到双端队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
    """
    时间复杂度：n，所有节点
    空间复杂度：n，所有节点，双端队列最多有n/2个元素，res会存储所有节点
    """