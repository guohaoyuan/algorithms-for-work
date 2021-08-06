"""
考虑两个问题：
    1. 当前节点做什么
    2. 什么时候做

第一个问题：
    不能简单比较当前节点和左右子节点的值；而是应该比较当前节点和左右子树节点的值，因此多了2）
    lower upper分别表示当前节点的上界和下界
    1）如果当前节点越界则False

    2）如果当前节点的左右子树也越界也是False

第二个问题：
    先序遍历，从根节点开始

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inorder(root, None, None)

    def inorder(self, root, lower_boundary, upper_boundary):
        if not root:
            return True

        if lower_boundary and lower_boundary.val >= root.val:
            return False
        if upper_boundary and upper_boundary.val <= root.val:
            return False
        left_t_f = self.inorder(root.left, lower_boundary, root)
        right_t_f = self.inorder(root.right, root, upper_boundary)
        
        if not left_t_f:
            return False

        if not right_t_f:
            return False

        return True 
