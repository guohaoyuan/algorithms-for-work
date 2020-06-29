# -*- coding = utf-8 -*-

import collections

class MaxQueue(object):

    def __init__(self):
        """
        初始化两个双端队列
        """
        self.queue = collections.deque()  # 存放正常数组
        self.maxQueue = collections.deque() # 维护一个非严格递减的队列

    def max_value(self):
        """
        直接取出最大值队列的头部
        :return:
        """
        return self.maxQueue[0] if self.maxQueue else -1

    def push_back(self, value):
        """
        维护非严格递减队列
        :param value:
        :return:
        """
        while self.maxQueue and self.maxQueue[-1] < value:
            self.maxQueue.pop() # 尾部元素弹出
        self.maxQueue.append(value)
        self.queue.append(value)

    def pop_front(self):
        """
        先判断是否为空；然后比较正常数组的头部是否是非严格递减数组的头部
        :return:
        """
        if not self.queue:
            return -1

        res = self.queue.popleft()
        if res == self.maxQueue[0]:
            self.maxQueue.popleft()
        return res

if __name__=='__main__':
    solution1 = MaxQueue()
    print(solution1.max_value())
    print(solution1.push_back(1))
    print(solution1.push_back(2))
    print(solution1.max_value())
    print(solution1.pop_front())
    print(solution1.max_value())
    print("==================")
    solution2 = MaxQueue()
    print(solution2.pop_front())
    print(solution2.max_value())