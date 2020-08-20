class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]表示到达当前位置所需的方法数
        # dp[i][j] = dp[i][j-1] + dp[i-1][j]    # 在中间
        #          = dp[i][j-1]                 # 第一行
        #          = dp[i-1][j]                 # 第一列
        #          = dp[0][0]                   # 左上角
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i== 0 and j > 0:
                    # 第一行
                    dp[i][j] = dp[i][j-1]
                elif i > 0 and j==0:
                    # 第一列
                    dp[i][j] = dp[i-1][j]
                else:
                    # 中间
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]