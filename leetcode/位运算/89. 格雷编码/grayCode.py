class Solution:
    def grayCode(self, n):
        # 1. 特殊情况: n等于0,则返回[0]
        if n == 0:
            return [0]

        # 2. 初始化返回结果
        res = []

        # 3. 算法流程利用格雷码的公式
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res

if __name__ == "__main__":
    n1 = 2
    solution = Solution()
    print(solution.grayCode(n1))
    """
    时间复杂度: 2^n
    空间复杂度:1
    """