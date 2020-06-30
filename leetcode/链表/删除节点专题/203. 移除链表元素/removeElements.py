# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        # 对于不是尾部的节点使用复制删除法,对于尾部节点就需要使用pre和cur指针
        # 由于头节点有可能使被删除的对象
        pre = None
        cur = head

        while True:
            if cur.val == val:
                # 不是tail
                if cur.next:
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                else:   # 是tail
                    if pre: # 长度可能为1
                        pre.next = None
                        return head
                    else:
                        return pre
                # 补充一点, 复制删除法有一个附加好处就是,相当于已经更新的cur指针
            else:
                # 由于不能确定要删除的val是否一定存在
                if cur.next:
                    pre = cur
                    cur = cur.next
                else:   #  要删除的值不存在
                    return head