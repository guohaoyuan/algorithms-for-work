# -*- coding : utf-8 -*-
import collections

class MyStack:
    """
    创建两个双端队列模拟栈，
    A存放数据
    B存除了A尾部最后一个元素以外的所有元素
    需要在进行”出栈操作“后，将两个双端队列进行互换
    关于“栈顶元素”，需要先pop存入tmp,再append(tmp)，返回tmp
    """
    def __init__(self):
        self.A = collections.deque()
        self.B = collections.deque()

    def push(self, x):
        self.A.append(x)

    def pop(self):
        if self.A:
            while len(self.A) > 1:
                self.B.append(self.A.popleft())
            # A中只剩队列尾巴，就是栈顶
            tmp = self.A.popleft()
            self.A, self.B = self.B, self.A
            return tmp
        else:   # A为空则直接返回
            return

    def top(self):
        if self.A:
            while len(self.A) > 1:
                self.B.append(self.A.popleft())
            # A只剩下一个尾巴
            tmp = self.A.popleft()
            self.B.append(tmp)
            self.A, self.B = self.B, self.A
            return tmp

    def empty(self):
        if self.A:
            return False
        else:
            return True