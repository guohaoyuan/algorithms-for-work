# -*- coding : utf-8 -*-

import collections


class MaxQueue:

    def __init__(self):
        """
        维护两个双端队列，第一个队列存储数据，第二个队列存放最大值
        """
        self.queue = collections.deque()
        self.max_queue = collections.deque()


    def max_value(self) -> int:
        """
        返回当前双端队列的最大值
        :return:
        """
        if not self.queue:
            return -1

        return self.max_queue[0]

    def push_back(self, value: int) -> None:
        """
        维护一个单调递减的双端队列
        :param value:
        :return:
        """
        # 1. 新数据会进入双端队列
        self.queue.append(value)

        # 2. 维护最大双端队列，单调递减
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()

        self.max_queue.append(value)

    def pop_front(self) -> int:
        """
        出队操作，如果存储元素的出队元素==辅助队列的队首元素，才出队
        :return:
        """
        # 判断是否为空
        if not self.queue:
            return -1

        res = self.queue.popleft()
        if res == self.max_queue[0]:
            self.max_queue.popleft()
        return res

if __name__ == "__main__":
    solution = MaxQueue()
    solution.push_back(1)
    solution.push_back(2)
    print(solution.max_value())
    solution.pop_front()
    print(solution.max_value())