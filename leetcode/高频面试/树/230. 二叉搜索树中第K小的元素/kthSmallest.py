# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.res = 0
        self.count = 0

        # 定义中序遍历
        def helper(root, k):
            if not root:
                return

            helper(root.left, k)
            # self.res.append(root.val)
            self.count += 1
            if self.count == k:
                self.res = root.val
            helper(root.right, k)

        if not root:
            return

        helper(root, k)
        return self.res