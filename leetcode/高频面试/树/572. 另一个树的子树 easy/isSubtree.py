"""
判断一个树为另一个树的子树，分三种情况：
    1. 妖魔两颗树相等，
    2. 妖魔t是s的左子树
    3. 妖魔t是s的右子树

两颗树是否相等：
    1. 如果有一个为空，就不相等
    2. 如果同时为空，则相等
    3. 如果两颗树都存在，则根节点相同 and 递归左子树相同 and 右子树相同
判断s是否为t的子树：
    1. 妖魔两颗树一个为空，一个存在，就不行
    2. 都为空，就就可以
    3. 如果两颗树都存在，则返回两颗树相同或者是左子树或者是右子树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and t:
            return False
        if not t and s:
            return False
        if not s and not t:
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSame(s, t)
    def isSame(self, s, t):
        if not s and t:
            return False
        if not t and s:
            return False
        if not t and not s:
            return True
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)