# -*- coding : utf-8 -*-

class Solution:
    def myPow(self, x, n):
        # 1. 特殊情况：x为零或者n为负数
        if x == 0 or x == 1:
            return x

        if n < 0:
            x = 1 / x
            n = - n

        # 2. 初始化返回结果
        res = 1


        # 3. 算法流程
        while n:
            if n & 1:
                res *= x

            x *= x
            n >>= 1
        return res

if __name__ == "__main__":
    x1 = 2.00
    n1 = 10
    x2 = 2.1
    n2 = 3
    x3 = 2.0
    n3 = -2
    solution = Solution()
    print(solution.myPow(x1, n1))
    print(solution.myPow(x2, n2))
    print(solution.myPow(x3, n3))
"""
时间复杂度：logn，快速幂运算
空间复杂度：1
"""