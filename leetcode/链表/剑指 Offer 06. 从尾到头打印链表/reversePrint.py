"""
遍历链表, 将结果存入列表
最后返回
"""
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        cur = head
        res = []

        while True:
            if cur:
                res.append(cur.val)
                cur = cur.next
            else:
                return res[::-1]