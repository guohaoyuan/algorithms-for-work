# -*- coding : utf-8 -*-
import collections

class Solution(object):
    def levelOrder(self, root):
        """
        迭代方式
        :param root:
        :return:
        """
        # 1.特殊情况：根节点为空
        if not root:
            return []

        # 初始化变量 返回结果用列表，暂存节点有双端队列、
        res = []
        queue = collections.deque()
        queue.append(root)

        # 3. 算法流程
        while queue:
            # 我们现将以一个临时列表存储本层的值
            tmp = []

            n = len(queue)
            for i in range(n):
                # 节点出栈
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
