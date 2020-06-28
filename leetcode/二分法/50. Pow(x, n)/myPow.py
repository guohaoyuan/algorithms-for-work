"""
1. 特殊情况, x如果是负数,则取倒数, n取相反数
2. 初始化res = 1用于存储返回结果
3. while n
        如果n是奇数, res = res * x
        x = x*x
        n = n // 2
"""

class Solution:

    def myPow(self, x, n):
        # 1. 特殊情况: x = 0
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = - n

        # 2. 初始化 res作为返回结果
        res = 1

        # 3. 快速幂
        while n:
            if n & 1 == 1:  # 是奇数
                res *= x

            x = x * x
            n = n >> 1
        return res


if __name__ == '__main__':
    x1 = 2.0
    n1 = 10
    x2 = 2.1
    n2 = 3
    x3 = 2

    solution = Solution()
    print(solution.myPow(x1, n1))
    print(solution.myPow(x2, n2))