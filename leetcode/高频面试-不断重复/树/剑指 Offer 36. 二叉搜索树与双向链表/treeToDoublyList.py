"""
第一反应是利用中序遍历，递归过程将前后链表连接起来
但是需要两个指针记录下整个个链表的头节点和尾节点
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
        if not root:
            return root

        # 创建两个指针记录头节点和尾节点
        # 一般连接节点都会用到当前节点和前一节点
        self.pre, self.head = None, None

        # 定一个函数进行中序遍历
        def helper(root):
            if not root:
                return
                # 遍历过程一般不需要返回值

            helper(root.left)
            # 如果是一开始，没有前继，需要初始化前继
            if not self.pre:
                self.pre = root
                self.head = root
            else:
                # 此时已经是中间部分，需要连接当前节点和前继
                self.pre.right = root
                root.left = self.pre
                # 更新前继
                self.pre = root
            # root当前节点的更新，隐含在递归中
            helper(root.right)

        helper(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head