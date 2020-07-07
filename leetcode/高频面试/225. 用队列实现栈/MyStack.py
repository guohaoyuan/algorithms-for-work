"""
使用一个队列实现栈

对于push(x)方法，
            直接将x入队，并记录队尾元素top_x，方便在top函数中返回

对于top（）方法
            直接返回队尾元素top_X

对于pop() 方法
            首先获得尺寸size
            while size >2:
                将队列头部元素取出放在队列尾
            更新top_x的指向
            然后将头部元素取出放在尾部
            # 此时头部的元素就是一开始的队尾元素
            删除头部元素

对于empty()方法
            只有队列为空时，才能为空
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.top_x = None
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        # 记录队尾元素
        self.top_x = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)

        while size > 2:
            self.queue.append(self.queue.popleft())
            size -= 1

        # 更新队尾元素
        self.top_x = self.queue[0]

        self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()