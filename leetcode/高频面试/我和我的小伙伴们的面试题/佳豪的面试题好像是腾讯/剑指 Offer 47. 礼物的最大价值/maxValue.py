"""
动态规划：
1. 定义状态:dp[i][j]表示到达当前位置所能得到的最大价值
2. 定义转移方程：
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j] 表示在中间
                 = dp[i-1][0] + grid[i][0]                  表示第一列只能从上面过来
                 = dp[0][j-1] + grid[0][j-1]                表示第一行只能从左边过来
3. base case dp[0][0] = grid[0][0]
"""

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # 原地修改，连初始状态都省了
        dp = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:   # 第一种情况：在第一行第一列，初始位置
                    continue
                elif i == 0 and j != 0: # 第二种情况：在第一行，只能从左位置到本位置
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0: # 第三种情况：在第一列，只能从上面位置到本位置
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:                   # 第四种情况：不在第一行第一列
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]