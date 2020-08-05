"""
建立虚拟头节点：
        1. 建立虚拟头节点，进位标识符
        2. 如果两个链表有一个存在时，
            得到当前位两个链表的节点值
            计算两节点的和
            计算是否进位，是商
            创建新节点，是余数
            后移新链表指针
            更新两个链表的指针
        3. 考虑最后一组链表会不会出现进位
        4. 返回虚拟节点的下一位
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        head1 = l1
        head2 = l2
        flag = 0
        dummy = ListNode(0)
        cur = dummy

        while head1 or head2:
            x = head1.val if head1 else 0
            y = head2.val if head2 else 0
            val = flag + x + y
            flag = val // 10    # 商
            val = val % 10      # 余数
            cur.next = ListNode(val)

            # 更新三个链表的指针
            cur = cur.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        # 均为空，要查看是否进位
        if flag:
            cur.next = ListNode(flag)
        return dummy.next

"""
两者思路一样，只是后者是自己想出来的
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        head = dummy
        shang = 0

        while p1 or p2:
            # 针对不同情况，进行求和
            if not p1:
                tmp = p2.val + shang
            if not p2:
                tmp = p1.val + shang
            if p1 and p2:
                tmp = p1.val + p2.val + shang

            # 判断求和是否大于10
            if tmp >= 10:
                shang, yu = 1, tmp % 10
            else:
                shang, yu = 0, tmp % 10
            # 创建节点
            head.next = ListNode(yu)

            # 更新三个链表的指针
            head = head.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        # 处理最后的进位
        if shang:
            head.next = ListNode(shang)
        return dummy.next