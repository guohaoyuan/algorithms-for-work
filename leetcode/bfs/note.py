"""
bfs框架

1. 特殊情况：

2. 创建一个双端链表，collections.deque()

3. 创建根节点，根节点入队

4. while queue: # 该条件不是固定的，例如反序列化时，需要保证i < n

        计算当前队列的长度size，其目的是让同一层，在for循环中依次被处理

        for index in range(size):
            cur = queue.popleft()

            此处根据需要对当前节点进行处理，# 比如，求得当前层的最大值，将当前层的节点存储到一个列表中

            如果左子树存在，左子树入队   # 如果是反序列化，其中会出现null，我们应该是判断i < n and res[i] != null ，左子树入队，更记得更新i；在序列化中则是cur存在就左子树入队

            如果右子树存在，右子树入队   # 同上
            # 另外，如果实际算树的深度，直接将当前节点和depth打包元组进入队列

5. 返回结果
"""