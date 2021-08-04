"""
1. 二叉搜索数，都是已经排好序的结构，我们很自然利用中序遍历，得到一个有序数组

2. 老办法
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def middle_order(self, root, res):
        if not root:
            return res
        
        self.middle_order(root.left, res)
        res.append(root.val)
        self.middle_order(root.right, res)

        return res
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        res = self.middle_order(root, res)
        n = len(res)

        if n < 2:
            return False
        
        L = 0
        R = n - 1

        while L < R:
            sum_two = res[L] + res[R]
            if sum_two== k:
                return True
            elif sum_two > k:
                R -= 1
            else:
                L += 1
        
        return False
