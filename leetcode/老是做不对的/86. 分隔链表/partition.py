"""
首先夸一下自己，独立写出题解

面试要求： 不能使用虚拟头节点
1. 特殊情况
2. 初始化五个指针
                small, 小节点指针
                smallhead, 小节点头节点
                big, 大节点指针
                bighead, 大节点头节点
                cur 当前指针
3. 当前指针存在情况下:
    while cur:
        如果是小节点：
            我们应该先判断是不是第一次出现小节点
            if not small:
                初始化小节点和小节点头节点
            else:
                不是第一次出现，我们应该连接小节点指针，更新小节点指针
                small.next = cur
                small = cur
            更新当前节点
        如果是大节点：
            我们应该先判断是不是第一次出现大节点
            if not big:
                初始化大节点和大节点头节点
            else:
                不是第一次出现，我们应该连接大节点指针，更新大节点指针
                big.next = cur
                big = cur
            更新当前节点
    # 此时cur已经为none， 我们需要根据两个头节点是否存在来拼接
    我们需要判断小节点头节点是否存在
        直接向小节点指针指向大节点 头节点
    我们需要判断大节点是否存在
        大节点指针指向空
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 1. 特殊情况：数组为空
        if not head:
            return head

        # 2. 定义small,big
        small, smallHead = None, None
        big, bigHead = None, None
        cur = head

        # 3. 算法流程：
        # 我们在遍历过程更新链表，并连接，类似奇偶链表
        while cur:
            if cur.val < x:
                if not small:
                    # 第一次遇到小节点，初始化
                    small = cur
                    smallHead = cur
                else:
                    # 至少是第二次遇到
                    small.next = cur
                    # 更新small 指针
                    small = cur
                # 更新当前指针
                cur = cur.next
            else:
                if not big:
                    # 第一次遇到大节点，初始化
                    big = cur
                    bigHead = cur
                else:
                    # 至少是第二次遇到
                    big.next = cur
                    big = cur
                cur = cur.next

        # 此时cur为空
        if smallHead:
            # 如果小节点存在
            small.next = bigHead

        if bigHead:
            # 如果大节点存在
            big.next = None

        return smallHead if smallHead else bigHead

"""

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        odd, even = None, None
        p3 = head  # 主指针，过链表
        p1 = None
        p2 = None
        while True:
            if p3.val < x:
                # 初始化左链表
                if not odd:
                    odd = p3
                    p1 = p3
                else:
                    p1.next = p3
                    p1 = p1.next
                p3 = p3.next
            else:
                if not even:
                    even = p3
                    p2 = p3
                else:
                    p2.next = p3
                    p2 = p2.next
                p3 = p3.next
            if not p3:
                if p1 and p2:
                    p2.next = None
                    p1.next = even
                    return odd
                if p1:
                    return odd
                if p2:
                    return even
