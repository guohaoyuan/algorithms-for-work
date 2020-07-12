"""
递归需要建立一个辅助函数helper(res, root)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(res, root):
            if not root:
                return []
            helper(res, root.left)
            res.append(root.val)
            helper(res, root.right)
            return res

        res = []
        return helper(res, root)

"""
利用压栈来模拟递归
因此进栈顺序应该是和期待顺序相反的
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 特殊情况：根节点为空
        if not root:
            return []

        # 创建一个栈用于存放状态和节点;创建一个列表存放结果
        stack = [(root, 'white')]
        res = []

        #
        while stack:
            node, color = stack.pop()

            if not node:
                continue

            if color == 'gray':
                res.append(node.val)
            else:
                stack.append((node.right, 'white'))
                stack.append((node, 'gray'))
                stack.append((node.left, 'white'))
        return res
