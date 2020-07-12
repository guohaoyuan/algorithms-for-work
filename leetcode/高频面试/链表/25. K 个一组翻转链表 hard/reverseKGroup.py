"""
这个题应该和206一起看，记得每次实现一个函数用一个简单用例测试一下

1. 特殊情况有两种k==1或者为空链表

2. 初始化dummy,dummy.next = head
        pre = dummy
        start = head
        end = head

3. 在while True:中循环
        首先找到end的位置
        for i in range(k - 1)
            需要保证end.next存在才能执行end.next
            if end and end.next:
                end = end.next
            如果在后移end过程发现不足k，直接返回dummy.next
        此时end比存在
        nt   = end.next # next指针
        end = None # 将其断开，方便翻转
        pre.next = reverse(start)
        需要将链表连接回去
        start.next = nt
        更新start指针，end指针，pre指针
        pre = start
        start = nt
        end = nt

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(node):
            if not node or not node.next:
                return node
            pre = None
            cur = node
            nt = node.next

            while True:
                if not nt:
                    cur.next = pre
                    return cur
                cur.next = pre
                pre = cur
                cur = nt
                nt = nt.next

        # 1. 特殊情况：空链表
        if not head:
            return head
        if k == 1:
            return head
        # 2. 初始化三个指针start, end, nt
        start, end, nt = head, head, None
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        # 3. 算法流程
        while True:
            for i in range(k - 1):
                if end and end.next:
                    # end指针在这里更新
                    end = end.next
                else:
                    return dummy.next
            # nt指针在这里更新
            nt = end.next
            end.next = None
            pre.next = reverse(start)
            start.next = nt

            # 更新指针
            pre = start
            start = nt
            end = start



"""
1. 特殊情况： 空链表
             k==1
    
2. 初始化dummy.next = head
        start, end = head, head
        pre = dummy
        nt = none

3. 定义翻转函数：
    递归结束条件
    
4. 算法流程
    循环k-1次，
        在这个过程必须当前位置end存在且end.next存在，才能更新end;
                                    否则，不足k直接返回
        
        然后我们需要更新指针nt
        如果end.next存在，nt = end.next
                    否则，nt=none
        此时翻转start, end, 需要现将其断开,end.next = none
        pre.next = reverse(start)
        此时需要将其连接回去,
                    如果nt存在，start.next = nt
                            更新pre = start
                            start, end = nt, nt
                    否则，start.next = none
                        return dummy.next
        
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        start, end = head, head
        pre = dummy
        nt = None

        def reverse(head):
            if not head or not head.next:
                return head

            pre = None
            cur = head
            nt = head.next

            while True:
                if not nt:
                    cur.next = pre
                    return cur
                cur.next = pre
                pre = cur
                cur = nt
                nt = nt.next

        while True:
            for i in range(k - 1):
                if end and end.next:
                    end = end.next
                else:
                    return dummy.next

            if end and end.next:
                nt = end.next
            else:
                nt = None

            end.next = None
            pre.next = reverse(start)
            if nt:
                start.next = nt
                pre = start
                start = nt
                end = nt

            else:
                start.next = None
                return dummy.next

