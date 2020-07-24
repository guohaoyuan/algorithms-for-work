"""
bfs
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"

        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()

                if cur:
                    res.append(str(cur.val))
                else:
                    res.append("null")

                if cur:
                    queue.append(cur.left)
                if cur:
                    queue.append(cur.right)

        return "[" + ','.join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data[1:-1]
        # 特殊情况[""]
        if not res:
            return None
        # 其中还是字符串
        res = res.split(',')
        queue = collections.deque()
        root = TreeNode(int(res[0]))
        queue.append(root)
        i = 1  # 遍历res
        n = len(res)

        while i < n and queue:
            size = len(queue)

            for _ in range(size):
                cur = queue.popleft()

                # 我们不会创建一个空节点，所以不需要处理当前节点

                # 我们看下一个节点是否存在
                if i < n and res[i] == "null":
                    i += 1
                else:
                    # 创建节点，并入队
                    cur.left = TreeNode(int(res[i]))
                    queue.append(cur.left)
                    i += 1

                if i < n and res[i] == "null":
                    i += 1
                else:
                    cur.right = TreeNode(int(res[i]))
                    queue.append(cur.right)
                    i += 1
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        data = data[1:-1].split(',')

        queue = collections.deque()
        root = TreeNode(int(data[0]))
        queue.append(root)
        i = 0
        n = len(data)

        while queue and i < n:
            size = len(queue)
            for index in range(size):
                cur = queue.popleft()

                if data[i + 1] != "null":
                    left = TreeNode(int(data[i + 1]))
                    queue.append(left)
                    cur.left = left
                    i += 1
                else:
                    i += 1

                if data[i + 1] != "null":
                    right = TreeNode(int(data[i + 1]))
                    queue.append(right)
                    cur.right = right
                    i += 1
                else:
                    i += 1
        return root