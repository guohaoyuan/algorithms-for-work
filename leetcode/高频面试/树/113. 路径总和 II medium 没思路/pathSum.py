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

        def helper(root, sum, path):
            if not root:
                return

            if not root.left and not root.right and sum - root.val == 0:
                path.append(root.val)
                res.append(path[:])
                return

            # 因为必须从根节点出发到叶子节点，所以path和sum都是必须进行更新的
            helper(root.left, sum - root.val, path + [root.val])
            helper(root.right, sum - root.val, path + [root.val])

        helper(root, sum, path)
        return res