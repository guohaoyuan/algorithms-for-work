# -*- coding: utf-8 -*-
import math

class Solution(object):

    def cuttingRope(self, n):
        """
        贪心算法
        :param int:
        :return:
        """
        # 1. 特殊情况：n为2或3
        if n <= 3:
            return n - 1

        # 2. 初始化商和余数
        a, b = n // 3, n % 3

        # 3. 算法流程
        if b == 0:  # 余数为0,全部是3就好了
            return int(math.pow(3, a))
        if b == 1:  # 余数为1,最后两端为2*2
            return int(math.pow(3, a -1) * 4)
        if b == 2:  # 余数为2,最后一段为2就好
            return int(math.pow(3, a) * 2)

if __name__ == '__main__':
    test1 = 2
    test2 = 10
    solution = Solution()
    print(solution.cuttingRope(test1))
    print(solution.cuttingRope(test2))
    """
    时间复杂度：1，math。pow调用C库执行浮点运算，时间复杂度1
    空间复杂度：1,常数级别的变量，1
    """