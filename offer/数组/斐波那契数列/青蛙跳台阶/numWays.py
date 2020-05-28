# -*- coding = utf-8 -*-

class Solution:

    def numWays(self, n):
        """
        当n = 0 return 1 ; n = 1 return 1 ; n = 2 return 2 ; n = 3 return F1 + F2 = 3 ; n = 4 return F2 + F3 = 5
        :param n: int 输入几阶台阶
        :return: int 跳法有几种
        """
        # 1. 特殊情况 0 1 2
        if n < 2:
            return 1

        # 2. 初始化
        f0 = 1
        f1 = 1

        # 3. 算啊流程：可以看出是从f1开始不是f0
        for i in range(2, n + 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return fn % 100000007

if __name__ == "__main__":
    n = 5
    fn = Solution().numWays(n)
    print(fn)