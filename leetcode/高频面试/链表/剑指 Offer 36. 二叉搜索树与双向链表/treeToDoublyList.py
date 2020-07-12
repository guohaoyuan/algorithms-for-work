"""
树转链表

一般情况二叉搜索树与中序遍历有关系

1. 特殊情况

2. 创建头节点self.head, 前向指针self.pre

3. 递归调用中序遍历
    在递归操作部分：
                如果前向节点没初始化，初始化头节点self.head
                如果前向节点初始化，将当前指针cur和pre进行连接
                    self.pre.right = cur
                    cur.left = se;f.pre

                更新前向指针
                    self.pre = cur

                关于更新cur指针在递归操作中
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 1. 特殊情况：
        if not root:
            return root
        # 2. 初始化头节点和前向指针
        self.head = None
        self.prev = None

        # 3. 定义中序遍历的递归函数
        # 在函数中需要进行双向链表的连接
        def helper(node):
            if not node:
                return

            helper(node.left)

            if not self.prev:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev

            # 更新前向指针
            self.prev = node

            # 更新当前指针
            helper(node.right)

        helper(root)

        # 连接首尾
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head