"""
快速幂解法，需要自定义矩阵乘法;需要利用快速幂解法


自定义矩阵乘法，步骤：
    1. 初始化一个空矩阵
    2. 三层遍历，第一层是行，第二层是列，第三层是计算过程
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j]+=input1[i][k]*input2[k][j]
    3. 返回res


快速幂：是一种自下而上的
    1. 初始化单位矩阵res[[1, 0][0, 1]]和基础矩阵A[[1, 1][1, 0]]
    2. while n:
            if n & 1:
                res = mul(A, res)
            A = mul(A, A)
            n = n >> 1
    3. return res[0][1]
"""

class Solution:
    def Fibonacci(self, n):
        def mul(A, B):
            res = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        res[i][j] += A[i][k] * B[k][j]
            return res

        if n <= 1:
            return n

        res = [[1, 0], [0, 1]]
        A = [[1, 1], [1, 0]]

        while n:
            if n & 1:
                res = mul(res, A)
            A = mul(A, A)
            n = n >> 1
        return res[0][1]

if __name__ == '__main__':
    test1 = 6
    solution = Solution()
    print(solution.Fibonacci(test1))