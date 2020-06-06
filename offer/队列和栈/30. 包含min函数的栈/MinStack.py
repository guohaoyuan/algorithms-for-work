# -*- coding : utf-8 -*-

class MinStack:
    """
    维护一个实时的最小值栈self.B
    """
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)
        # 如果b为空，或者b的栈顶元素>=x，入B
        if not self.B or self.B[-1] >= x:
            # 非严格递减
            self.B.append(x)

    def pop(self):
        tmp = self.A.pop()
        if tmp == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]

class MinStack_v2:
    """
    维护一个等长的最小值栈self.B
    """
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)
        # 如果此时栈为空，或者当前栈顶元素比较大，需要加入新元素
        if not self.B or self.B[-1] > x:
            self.B.append(x)
        elif self.B[-1] <= x:
            self.B.append(self.B[-1])

    def pop(self):
        self.A.pop()
        self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]