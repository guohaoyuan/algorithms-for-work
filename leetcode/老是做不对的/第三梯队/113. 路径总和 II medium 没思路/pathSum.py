# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []
        res = []
        path = []

        def helper1(root, sum, path):

            if not root:
                return
            if not root.left and not root.right:
                if sum - root.val == 0:
                    path.append(root.val)
                    res.append(path)
                return
            helper1(root.right, sum - root.val, path + [root.val])
            helper1(root.left, sum - root.val, path + [root.val])

        helper1(root, sum, path)

        return res