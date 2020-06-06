# -*- coding : utf-8 -*-

class MyQueue:
    """
    用两个栈实现队列，大体上，栈A存放数据，然后转移到B中，B中得到的就是经过逆序的A，可以当作队列使用
    """
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)

    def pop(self):
        # 1. 如果b不为空，则B出栈
        if self.B:
            return self.B.pop()
        # 2. 如果B为空，A不为空，A进入B
        if not self.B and self.A:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()
        # 3. 如果A B均为空，则返回
        if not self.A and not self.B:
            return

    def peek(self):
        # 1. 如果b不为空，则返回B栈顶
        if self.B:
            return self.B[-1]

        # ## 曲线救国
        # if self.B:
        #     tmp = self.B.pop()
        #     self.B.append(tmp)
        #     return tmp
        #
        # 2. 如果B为空，A不为空，则A进入B
        if not self.B and self.A:
            while self.A:
                self.B.append(self.A.pop())
            return self.B[-1]
        # 3. 如果均为空，则返回
        if not self.A and not self.B:
            return

    def empty(self):
        if not self.A and not self.B:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = MyQueue()
    solution.push(1)
    solution.push(2)
    print(solution.A, solution.B)
    print(solution.peek())
    print(solution.pop())
    print(solution.empty())