"""

首先，需要明确两个问题：
    1. 以当前节点为根的二叉树子树长什么样
    2. 以其他节点为根的子树长啥样
然后，需要考虑什时候做：
    后续遍历做


对于第一个问题，
    考虑要知道左右子树，确定用后续遍历
    考虑要知道左右子树的样子，确定需要对于当前节点记录左右子树的样子，拼接为字符串
        对于空指针的情况我们采用#表示，节点间使用,分离


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):

    def __init__(self):
        # 记录所有子树以及出现次数
        self.memo = collections.defaultdict(int)
        # 记录重复的子树根节点
        self.res = []
   
    def traverse_tree(self, root):
        # 对于空节点，用字符#代替
        if not root:
            return "#"
        
        # 将左右子树序列化为字符串
        left_string = self.traverse_tree(root.left)
        right_string = self.traverse_tree(root.right)

        # 左右子树加上自己，就是当前节点为根节点的二叉树序列化结果
        sub_tree = left_string + "," + right_string + "," + str(root.val)

        # 查看是否之前出现过字典中
        freq = self.memo[sub_tree]

        
        # 如果出现了就加入结果；多次出现也只加入res 1次
        if freq == 1:
            self.res.append(root)
        
        # 给对应子树出现次数＋1
        self.memo[sub_tree] += 1

        return sub_tree

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.traverse_tree(root)
        return self.res
