"""
需要解决跨父节点的子节点相连

要细化到每一个节点需要做的事情

既然一个递归无法实现，就采用两个递归函数

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
        
    def connect_two_node(self, node1, node2):
        """
        负责连接每一个节点
        """
        if not node1 or not node2:
            return 
        
        # 将传入的两节点连接
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.connect_two_node(node1.left, node1.right)
        self.connect_two_node(node2.left, node2.right)

        # 连接跨越父节点的两个子节点
        self.connect_two_node(node1.right, node2.left)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        self.connect_two_node(root.left, root.right)
        
        return root
