# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def helper(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            dummy = ListNode(0)
            cur = dummy
            p1, p2 = node1, node2
            while p1 and p2:
                if p1.val >= p2.val:
                    cur.next = ListNode(p2.val)
                    cur = cur.next
                    p2 = p2.next
                else:
                    cur.next = ListNode(p1.val)
                    cur = cur.next
                    p1 = p1.next
            while p1:
                cur.next = ListNode(p1.val)
                cur = cur.next
                p1 = p1.next
            while p2:
                cur.next = ListNode(p2.val)
                cur = cur.next
                p2 = p2.next
            return dummy.next

        n = len(lists)

        def MergeSort(nums, l, r):
            if l == r:
                return nums[l]
            if l > r:
                return
            if l < r:
                mid = (l + r) >> 1
                l1 = MergeSort(nums, l, mid)
                l2 = MergeSort(nums, mid + 1, r)

                return helper(l1, l2)

        return MergeSort(lists, 0, n - 1)