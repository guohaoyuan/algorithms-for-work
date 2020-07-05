"""
时间复杂度: n, 遍历了所有节点
空间复杂度: n, 最糟糕的情况是最后一层的节点数n/2,
"""
import collections


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        depth = 1

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1

        return depth


"""
递归操作,一半看递归一步的情况,如果根节点和左右子树
二叉树的最小深度,要求到达最近的叶子节点

递归结束条件是: 当前节点为空,则直接返回 0
递归操作是: 当前节点的左右子树的深度
返回是:
如果当前节点的左右子树都为空,则取左右深度最小的+1, 其中1表示根节点
如果当前节点的左右子树有一个不为空,则取左右子树深度的和 + 1, 其中1表示根节点

时间复杂度: n
空间复杂度: logn, 树的高度
"""


class Solution1:
    def minDepth(self, root):
        if not root:
            return 0

        depth_left = self.minDepth(root.left)
        depth_right = self.minDepth(root.right)

        return min(depth_right, depth_left) + 1 if root.left and root.right else depth_left + depth_right + 1