"""
初始化两个链表的节点，
遍历链表，到头就去对面链表上跑步
当两者 相等时，结束，判断相等是None还是有节点


判断条件是p1存在就p1.next，因为这样保证可以取到none;
另外到头对面跑步，这一点需要注意
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB

        while True:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next if p1 else headB
                p2 = p2.next if p2 else headA
