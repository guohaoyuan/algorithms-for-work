"""
题干条件说明

所有节点唯一值,且只给出当前节点

步骤
我们用后一个节点覆盖当前节点的值
然后将后一个节点断开
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_next = node.next
        node.val = node_next.val
        node.next = node_next.next
        node_next.next = None