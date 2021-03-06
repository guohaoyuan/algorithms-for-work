"""
这个动态规划是从头更新的，初始化base case;也在遍历中实现

我们只处理，matrix[i][j] == '1'对应的dp[i][j]
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]表示当前位置的最大边长
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1  if matrix[i][j] == 1
        #           # 表示左边，上边，左上三个最小的边长+1
        # 第一行第一列就看是否为1或0
        if not matrix:
            return 0

        max_len = 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 考虑多行多列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        area = max_len * max_len
        return area

"""
做了小小的自适应
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]表示当前位置的边长
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        #          = 第一行第一列均是保持原值
        max_len = 0
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) == 0:
                    continue
                if i > 0 and j > 0 and int(matrix[i][j]) == 1:
                    dp[i][j] = min(int(dp[i][j - 1]), int(dp[i - 1][j - 1]), int(dp[i - 1][j])) + 1
                if max_len < dp[i][j]:
                    max_len = dp[i][j]
        return max_len * max_len