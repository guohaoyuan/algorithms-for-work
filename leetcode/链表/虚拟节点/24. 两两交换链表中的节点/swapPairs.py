"""

  0      1   ->    2     ->      3   ->      4       ->  None
dummy   start       end

需要保证start和end都要存在

1. 建立虚拟头节点,tmp指向虚拟头节点
2. while tmp.next and tmp.next.next
        start = tmp.next
        end = tmp.next,next

        # 翻转1 2
        tmp.next = end
        start.next = end.next
        end.next = start

        # 更新tmp. start, end
        tmp = start

3. 返回头节点
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1. 链表为空，或者长度不足2
        if not head or not head.next:
            return head

        # 2。创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        # 3.
        while tmp.next and tmp.next.next:
            start = tmp.next
            end = tmp.next.next

            # 交换链表中节点
            tmp.next = end
            start.next = end.next
            end.next = start

            # 更新tmp
            tmp = start
        return dummy.next