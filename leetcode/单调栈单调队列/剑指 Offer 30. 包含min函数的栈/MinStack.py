"""
维护一个同步辅助栈,空间换时间
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.source = []
        self.helper = []

    def push(self, x: int) -> None:
        self.source.append(x)
        if not self.helper or self.helper[-1] > x:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        self.source.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.source[-1]

    def min(self) -> int:
        return self.helper[-1]