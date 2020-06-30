"""

在链表内执行循环
"""
class Solution:
    def reverseList(self, head):
        if not head:
            return head

        pre = None
        cur = head
        nx = head.next

        while True:
            cur.next = pre

            if not nx:
                return cur
            else:
                pre = cur
                cur = nx
                nx = nx.next


"""
利用递归实现
1->2->3->4->none
其中1就是head, 
self.reverseList(head.next) 就是2<-3<-4, 其中last指向4
"""


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 返回最后一个节点
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last