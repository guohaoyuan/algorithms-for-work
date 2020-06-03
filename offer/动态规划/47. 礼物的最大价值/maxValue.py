# -*- coding : utf-8 -*-

class Solution(object):
    def maxValue(self, grid):
        """
        动态规划
        :param grid: 是个二维数组
        :return:
        """
        # 1. 特殊情况数组为空
        if not grid:
            return

        # 2. 初始化dp二维数组
        m = len(grid)   # 行
        n = len(grid[0])    # 列
        dp = grid           # 原地修改，看要求

        # 3. 根据动态转移方程更新dp
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:   # 第一种情况：在第一行第一列，初始位置
                    continue
                elif i == 0 and j != 0: # 第二种情况：在第一行，只能从左位置到本位置
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0: # 第三种情况：在第一列，只能从上面位置到本位置
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:                   # 第四种情况：不在第一行第一列
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    def maxValue2(self, grid):
        """
        上面的第一行第一列较为简单，如果单独拿出来初始化，会节省时间
        :param grid:
        :return:
        """
        # 1. 特殊情况：数组为空
        if not grid:
            return

        # 2. 初始化行列，动态规划数组dp，在原地修改
        m = len(grid)
        n = len(grid[0])
        dp = grid   # 由于是原地修改，所以第一步动态矩阵的初始化就在这里

        # 3. 算法流程：先初始化第一行第一列
        for i in range(1, m):  # 第一列
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):   # 第一行
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 初始化真个动态矩阵
        for i in range(1, m):
            for j in range(1, n):
                # 此时前三中情况均已解决，我们只剩下第四种情况
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    test1 = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    solution = Solution()
    print(solution.maxValue(test1))
    test1 = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    print(solution.maxValue2(test1))
    """
    首先这里测试再次让我意识到python向函数中传参是引用的副本，
    具体来说，对于可变数据类型，如列表，就是在原来的列表上修改
    对于不可变数据类型，如数字，就是产生一个副本，有新的地址空间，不影响原数字
    
    时间复杂度：mn
    空间复杂度：原地修改就是1,非原地修改就是mn
    """