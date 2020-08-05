# -*- coding : utf-8 -*-

class Solution:
    def fib(self, n):
        if n == 0:
            return 0

        # 定义矩阵乘法
        def mul(a, b):
            c = [[0, 0], [0, 0]]    # 定一个空矩阵存结果
            for i in range(2):      # 行
                for j in range(2):  # 列
                    for k in range(2):
                        c[i][j] += a[i][k] * b[k][j]
            return c

        # 初始化结果：
        # A1
        A = [[1, 1], [1, 0]]
        # 单位阵
        res = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                res = mul(A, res)
            A = mul(A, A)
            n >>= 1
        return res[0][1]

if __name__ == "__main__":
    n1 = 2
    n2 = 5
    solution = Solution()
    print(solution.fib(n1))
    print(solution.fib(n2))
    """
    时间复杂度：logn
    空间复杂度：1，常数级别的
    """