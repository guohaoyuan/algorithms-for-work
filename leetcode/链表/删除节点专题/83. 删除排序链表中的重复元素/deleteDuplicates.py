"""
小朋友,也许你有很多问号?

为什么while中的判断语句有时候为
                            if cur  # 为了判断当前元素, 主要是不涉及对尾部的特殊处理
                    有时候为
                            if cur.next # 为了判断是否是tail
"""


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # pre = None
        # cur = head

        # 由于head不会被处理,所以初始化pre可以为head
        pre = head
        cur = head.next

        while True:
            if cur:
                if cur.val == pre.val:
                    pre.next = cur.next
                    cur = cur.next
                else:
                    # 不相等
                    pre = cur
                    cur = cur.next
            else:
                # 表明已经到了tail
                return head