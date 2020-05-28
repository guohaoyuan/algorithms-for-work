# -*- coding = utf-8 -*-

from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here
        """
        # 创建A存储较大一半，为小顶堆
        self.A = []
        # 创建B存储较小一半，为大顶堆
        self.B = [] # 允许A的长度 最多比B大1

    def addNum(self, num):
        """
        添加元素
        :param num: int
        :return: 没有返回值
        """
        # 例如 A [3] B [2] 插入1
        if len(self.A) == len(self.B):
            heappush(self.B, - num)
            heappush(self.A, - heappop(self.B))
        else:   # 例如 A [3] B [] 插入4
            heappush(self.A, num)
            heappush(self.B, - heappop(self.A))

    def findMedian(self):
        """
        找到中位数
        :return: float
        """
        # 判断A B 长度
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0]) / 2.0
        else:
            return self.A[0]


if __name__ == '__main__':
    solution = MedianFinder()
    solution.addNum(1)
    solution.addNum(2)
    print(solution.findMedian())
    solution.addNum(3)
    print(solution.findMedian())
    solution1 = MedianFinder()
    solution1.addNum(2)
    print(solution1.findMedian())
    solution1.addNum(3)
    print(solution1.findMedian())
    '''
    时间复杂度：添加操作logN,因为堆插入和弹出操作时间复杂度logN；查找中位数1,获得堆顶元素时间复杂度1
    空间复杂度：N，数据流中元素数目'''