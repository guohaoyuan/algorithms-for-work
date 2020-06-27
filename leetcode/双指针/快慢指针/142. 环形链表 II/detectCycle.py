"""
分两步,首先判断链表是否有环
有环情况下,将其中一个节点归head, 两指针以相同速度遍历
再次相遇就是,入环节点
"""


class Solution:

    def detectCycle(self, head):
        if not head:
            return None

        slow, fast = head, head

        while True:
            # 一开始就判断是担心出现长度为1的链表
            if not fast or not fast.next:
                return None
            else:
                slow = slow.next
                fast = fast.next.next

            if slow == fast:
                break

        fast = head

        while True:
            # 一开始就判断是担心头节点就是答案
            if fast == slow:
                return fast
            else:
                fast = fast.next
                slow = slow.next
