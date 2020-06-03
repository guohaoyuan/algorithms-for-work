# -*- coding : utf-8 -*-


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None



class Solution(object):

    def buildTree(self, preorder, inorder):
        """

        :param preorder: 前序遍历的数组，
        :param inorder: 中序遍历的数组
        :return:
        """
        # 1. 结束条件：传入的先序列表为空或者传入的中序列表为空
        if not preorder or not inorder:
            return

        # 2. 递归操作
        # 首先初始化根节点
        root = ListNode(preorder[0])

        # 遍历中序列表找到对应的根节点
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                # 找到以后，开始递归，传入分段的先序和后序列表
                # 递归得到左子树
                root.left = self.buildTree(preorder[1: i + 1], inorder[:i])     # 先序遍历不包括0，对应根节点
                # 递归得到右子树
                root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])  # 后续遍历不包括i，对应根节点
                # 递归结束break
                break
        # 递归结束，我们开始返回值
        return root

if __name__ == '__main__':
    preorder1 = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder1 = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    recoverTree = solution.buildTree(preorder1, inorder1)
    print('\n',
          recoverTree.val, '\n',
          recoverTree.left.val, recoverTree.right.val, '\n',
          recoverTree.left.left.val, recoverTree.right.left.val, recoverTree.right.right.val, '\n',
          recoverTree.left.left.right.val, recoverTree.right.right.left.val)
    """
    时间复杂度：遍历每个节点，n
    空间复杂度：logn，递归深度
    """