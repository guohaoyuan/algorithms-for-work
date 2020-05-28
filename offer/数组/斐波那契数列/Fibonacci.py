# -*- coding = utf-8 -*-

class Solution(object):
    def Fibonacci(self, n):
        """
        举个具体的例子：n = 0 返回 0; n = 1 返回 1；n = 2 返回 1；
        利用动态规划，递推公式，Fn = Fn-1 + Fn-2
        :param n: 输入int数字
        :return: int数字
        """
        # 1. 特殊情况 小于2直接返回
        if n == 0 or n == 1:
            return n

        # 2. 初始化F0 F1
        f0 = 0
        f1 = 1

        # 3. 算法流程
        for i in range(2, n + 1):   # 注意n + 1
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return fn % 1000000007

if __name__ == '__main__':
    n = 6
    Fn = Solution().Fibonacci(n)
    print(Fn)
    '''
    分析时间复杂度：n
    空间复杂度：1
    '''