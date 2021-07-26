"""
使用一个队列实现栈。

直接将元素加入队列，同时记录队尾元素，因为队尾元素相当于栈顶元素，如果要 top 查看栈顶元素的话可以直接返回

push方法：
            数据结构是先进先出的队列，每次 pop 只能从队头取元素；但是栈是后进先出，也就是说 pop API 要从队尾取元素。
            把队列前面的都取出来再加入队尾，让之前的队尾元素排到队头，这样就可以取出了。
            这样实现还有一点小问题就是，原来的队尾元素被提到队头并删除了，但是 top_elem 变量没有更新，我们还需要一点小修改：size==2时候更新栈顶元素
            

初始化top_x表示队尾元素；
初始化一个空队列；

对于push(x)方法，
            直接将x入队，并记录队尾元素top_x，方便在top函数中返回

对于top（）方法
            直接返回队尾元素top_X

对于pop() 方法 
            首先获得原始队列尺寸size
            while size >2: 将队列尾的最后一个元素放到堆首
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


"""
在top操作中做了删除操作，不是很好，可以定义一个top全局变量
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)
        for _ in range(size - 1):
            tmp = self.queue.popleft()
            self.queue.append(tmp)
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp = self.pop()
        self.queue.append(tmp)
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue:
            return True
        else:
            return False


"""
属于自己的优化
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.topx = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.topx = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)
        for _ in range(size - 1):
            tmp = self.queue.popleft()
            self.queue.append(tmp)
            self.topx = tmp
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        # tmp = self.pop()
        # self.queue.append(tmp)
        # return tmp
        print(self.topx)
        return self.topx

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
