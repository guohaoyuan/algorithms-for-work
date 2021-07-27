"""
对于push(x)方法
    直接入栈

对于peek（）方法
    # 如果stack2不为空，则直接返回stack2[-1]；否则需要将stack1元素转移到stack2

对于pop()方法
    在弹出之前，先执行peek操作，以保证stack2存在元素
    直接删除stack2的栈顶元素，就是队列的头部

对于empty()方法
    只有两个栈都为空时， 才为空
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2 and self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
不得不承认，labuladong的代码很精练
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.helper:
            while self.data:
                self.helper.append(self.data.pop())
        tmp = self.helper.pop()
        return tmp

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.helper:
            while self.data:
                self.helper.append(self.data.pop())
        tmp = self.helper[-1]
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.helper and not self.data:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
每次方法都不一样，头大
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.helper:
            return self.helper.pop()
        while self.data:
            self.helper.append(self.data.pop())
        return self.helper.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.helper:
            return self.helper[-1]
        while self.data:
            self.helper.append(self.data.pop())
        return self.helper[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) == 0 and len(self.helper) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
