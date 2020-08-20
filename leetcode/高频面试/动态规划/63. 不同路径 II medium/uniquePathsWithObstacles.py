class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j]表示到达当前位置所需的方法数
        #
        # dp[i][j] = dp[i][j-1] + dp[i-1][j]    # 在中间, i-1, j和 i,j-1没有障碍物
        #
        #          = dp[i][j-1]                 # 第一行或者i-1,j有障碍物
        #          = dp[i-1][j]                 # 第一列或者i,j-1有障碍物
        #          = continue                   # 左上角或者当前位置有障碍物
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (obstacleGrid[i][j] == 1):
                    continue
                elif (i == 0 and j > 0) or (obstacleGrid[i-1][j] ==1):
                    dp[i][j] = dp[i][j-1]
                elif (i > 0 and j == 0) or (obstacleGrid[i][j-1] == 1):
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j > 0 and obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]