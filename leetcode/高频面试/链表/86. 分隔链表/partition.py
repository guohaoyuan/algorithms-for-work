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
        if not head:
            return head

        dummy = ListNode(0)
        p1 = dummy
        indummy = ListNode(0)
        tail = ListNode(0)
        p2 = indummy

        indummy.next = tail
        cur = head

        while True:
            node = ListNode(cur.val)
            if node.val < x:
                p1.next = node
                p1 = p1.next
            else:
                node.next = tail
                p2.next = node
                p2 = p2.next
            cur = cur.next
            if not cur:
                p2.next = None
                p1.next = indummy.next

                return dummy.next
"""
一半原地修改，不改变当前节点的指向，不破坏next指针，就会好转换到cur = cur.next
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        p1 = None
        p2 = None
        res1, res2 = None, None
        while True:
            if not head:
                break
            if head.val < x:
                if not p1:
                    p1 = head
                    res1 = head
                else:
                    p1.next = head
                    p1 = p1.next
                head = head.next
            else:
                if not p2:
                    p2 = head
                    res2 = head
                else:
                    p2.next = head
                    p2 = p2.next
                head = head.next
                if not head:
                    break
        if not res1:
            return res2
        if not res2:
            return res1
        p1.next = res2
        p2.next = None
        return res1