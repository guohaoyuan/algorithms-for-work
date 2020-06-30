"""
在while True:里面按照正常逻辑执行就行
"""


class Solution:

    def hasCycle(self, head):

        if not head:
            return False

        slow, fast = head, head

        while True:
            # 如果遇到结尾就跳出, 因为快慢指针,分奇数偶数节点情况, 所以需要not fast or not fast.next,
            # 遇到快慢指针, 这样做判断就是对的
            if not fast or not fast.next:
                return False
            else:
                fast = fast.next.next
                slow = slow.next

            if fast == slow:
                return True