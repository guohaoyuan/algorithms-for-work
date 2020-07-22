"""
只遍历一次链表

步骤：
    1. 特殊情况：当前链表为空或者只有一个节点，直接返回
    2. 初始化当前指针和下一个指针
    3. 遍历链表分两种情况：
                3.1 当前节点和下一个节点相等，则开始删除节点，每次删除节点以后需要判断下一节点是否为空，为空直接返回head
                3.2 当前节点和下一个节点不相等，则开始更新指针，每次更新节点以后需要判断下一节点是否空，为空直接返回head

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 1. 特殊情况节点为空
        if not head or not head.next:
            return head

        # 2. 初始化两个指针
        cur = head
        if head.next:
            nt = head.next

        while True:
            # cur与nt相等
            while cur.val == nt.val:
                cur.next = nt.next
                nt = nt.next
                # 此时可能nt.next=none
                if not nt:
                    return head

            # cur nt不相等
            while cur.val != nt.val:
                cur = nt
                nt = nt.next
                # 此时nt.next=none
                if not nt:
                    return head