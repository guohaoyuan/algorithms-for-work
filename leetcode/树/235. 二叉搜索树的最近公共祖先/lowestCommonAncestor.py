# -*- coding : utf-8 -*-

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """

        :param root: 根节点
        :param p: 节点p
        :param q: 节点q
        :return:
        """
        if root.val > p.val and root.val > q.val:
            # 公共父节点应该在左子树中
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            # 公共节点应该在右子树中
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # 就是当前节点
            return root
    """
    时间复杂度：n，遍历每一个节点
    空间复杂度：h，二叉树的深度，最优秀的情况为logn，最差的情况n"""

    def lowestCommonAncestor_v2(self, root, p, q):
        # 当前节点
        node = root

        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
    """
    时间复杂度：n，遍历每一个节点
    空间复杂度：1，没有递归，常数级别的常量
    """