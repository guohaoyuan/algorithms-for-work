"""
主要思想:区分两种情况:
    1. 不是tail, 我们直接将cur指针赋值为后一个节点, 将后一个节点删除；返回head
    2. 是tail, 我们已经设置好了pre指针,将pre指针指向none

详细情况:
    我们首先利用cur指针找到要删除的节点
        找到删除节点, 如果不是tail利用复制删除法,进行删除
                    是tail利用pre进行删除
        没找到删除节点,就更新cur和pre指针



细节是:
初始化pre = none
cur = head

个人思考: 为什么,没有考虑引入虚拟头节点?
因为对于要删除的节点如果为头节点, 我们直接使用复制删除法,不需要设置
"""


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        pre = None
        cur = head

        while True:
            if cur.val == val:
                if cur.next:
                    # 不是tail
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                else:
                    # cur.next为空, 表明为tail
                    pre.next = None
                    # 直接pre指none
                return head
            else:   # 当前节点不是删除节点
                pre = cur
                cur = cur.next