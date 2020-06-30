"""
这里用双指针,类似链表是否有环
让node1走到尾, 从headB开始;
让node2走到尾, 从headA开始;
分两种情况:  1. 有交点, 则这两者相等时, 返回
            2. 无交点, 则者两者相等时, 返回None
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node1 = headA
        node2 = headB

        while True:
            if node1 == node2:
                return node1
            # 不相交的情况下,让两者最后同时等于None
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA