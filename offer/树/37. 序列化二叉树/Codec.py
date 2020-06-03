# -*- coding : utf-8 -*-

import collections

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        """
        类似于面试题32
        :param root: 传入一棵树
        :return: 返回字符串
        """
        # 1. 特殊情况：根节点为空
        if not root:
            return "[]"

        # 2. 初始化变量返回结果暂存列表res，双端队列queue，并加入根节点
        res = []
        queue = collections.deque()
        queue.append(root)

        # 3. 算法流程
        while queue:
            # 3.1 首先获得当前节点
            node = queue.popleft()

            # 3.2 判断当前节点是否为空，为空则直接加入null到列表res，不为空则将当前节点先加入列表res，再左子树加入队列，右子树加入队列
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ','.join(res) + "]"

    def deserialize(self, data):
        """

        :param data: 是一个字符串
        :return: 返回一棵树
        """
        # 1. 特殊情况：字符串为空
        if not data:
            return

        # 2. 初始化先分割输入为列表res, 双端列表暂存根节点，索引i为1
        res = data[1: -1].split(',')
        i = 1
        queue = collections.deque()
        root = TreeNode(int(res[0]))
        queue.append(root)

        # 3. 算法流程
        while queue:
            # 3.1 首先将得到当前节点
            node = queue.popleft()

            # 3.2 判断res中当前位置！=null，分别创建左右子树,并更新queue
            if res[i] != 'null':
                node.left = TreeNode(int(res[i]))
                queue.append(node.left)
                i += 1
            else:
                i += 1

            if res[i] != 'null':
                node.right = TreeNode(int(res[i]))
                queue.append(node.right)
                i += 1
            else:
                i += 1
        return root