# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None

        def helper(root):
            if not root:
                return
            if not self.pre:
                self.pre = root
            else:
                self.pre.right = root
                self.pre.left = None
                self.pre = root

            # 因为在helper(root.left)中会修改root.right的指向，
            # 所以暂存right
            right = root.right
            helper(root.left)
            helper(right)

        helper(root)
