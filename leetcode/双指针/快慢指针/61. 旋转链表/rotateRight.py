"""
大体思路:
首先遍历链表求得长度
并在求得长度后,连接成环

对长度求余,
从head开始移动指针n-k-1位,得到新的尾巴和头部
将尾巴断开


计数n次,一般用for循环
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head

        cur = head
        count = 1

        while cur.next:
            count += 1
            cur = cur.next
        cur.next = head

        k = k % count
        # print(k, count)
        cur = head
        for i in range(count - k - 1):
            cur = cur.next
        new_head = cur.next

        cur.next = None
        return new_head