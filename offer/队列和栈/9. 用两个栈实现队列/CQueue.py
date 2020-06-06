# -*- coding : utf-8 -*-

class CQueue:

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value):
        """

        :param value:
        :return: none
        """
        self.A.append(value)


    def deleteHead(self):
        """

        :return: int 队首元素
        """
        if self.B:
            return self.B.pop()
        if not self.B and not self.A:
            return -1
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()