# -*- coding : utf-8 -*-
import collections

class Solution(object):

    def levelOrder(self, root):
        """

        :param root:
        :return:
        """
        # 1. 特殊情况：根节点为空
        if not root:
            return []

        # 2. 初始化返回结果列表，暂存节点双端队列
        res = []
        queue = collections.deque()
        queue.append(root)

        # 3. 算法流程
        while queue:
            # 建立双端队列
            tmp = collections.deque()

            # 迭代次数为每一层节点树
            n = len(queue)
            for i in range(n):
                # 双端队列先出队
                node = queue.popleft()
                # 判断res是奇数层还是偶数层
                if len(res) % 2 == 0:   # 偶数层
                    # 添加到双端队列tmp的尾部
                    tmp.append(node.val)
                else:                   # 奇数层则添加到双端队列的头部
                    tmp.appendleft(node.val)
                # 添加左右子节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(tmp))
        return res