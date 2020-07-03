"""
1. 利用快慢指针，找到中间节点
2. 构造翻转函数，将后半段翻转
3. 逐个比较前后两段，查看是否回文
4. 将后半段再次翻转，恢复原始连接
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. 特殊情况： 链表为空， 返回True
        if not head or not head.next:
            return True

        # 2. 利用快慢指针找到后半段
        slow, fast = head, head

        while True:
            # 此时，如果奇数节点，快指针到tail;如果是偶数节点，快指针到none
            if not fast or not fast.next:
                break

            slow = slow.next
            fast = fast.next.next

        # 如果是奇数，slow在后移一位
        if fast:
            slow = slow.next

        # 记录前半段尾部
        # print(slow, fast)

        # 3. 定义翻转链表函数
        def helper(node):
            # 只有一个节点直接返回
            if not node or not node.next:
                return node

            last = helper(node.next)
            node.next.next = node
            node.next = None
            return last

        new_head = helper(slow)
        left, right = head, new_head
        # print(left, right)
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True