"""
对于输入[1, 2, 3, 4, 5]构造bst

比如说选择3位根节点，这种情况下有多少BST
根据bst性质，左子树节点是[1, 2]的组合；右子树节点[3, 4]的组合
那么左子树组合*右子树组合就是3作为根节点时的bst个数

但是递归过程出现重复子问题，所以建立一个备忘录来记录重复子问题
"""

class Solution(object):

    def count_bst(self, left_boundry, right_boundry, memo):
        # 如果左边界大于右边界，因为递归时候要-1
        if left_boundry > right_boundry:
            return 1
        if memo[left_boundry][right_boundry] != 0:
            return memo[left_boundry][right_boundry]
        
        # 初始化返回结果res，表示当前根节点的bst数目
        res = 0

        # 遍历每一个节点并计算其bst数目
        for i in range(left_boundry, right_boundry + 1):
            left_bst_number = self.count_bst(left_boundry, i - 1, memo)
            right_bst_number = self.count_bst(i + 1, right_boundry, memo)
            res += left_bst_number * right_bst_number
        memo[left_boundry][right_boundry] = res

        return res

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        return self.count_bst(1, n, memo)
