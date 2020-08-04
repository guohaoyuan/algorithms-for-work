"""
完全背包问题：
初始化dp横纵多一行

1. 定义状态
        dp[i][j] 表示从前i个 硬币中挑选，组成目标为j的方法数

2. base case
        dp[0][..]没有硬币，则方法数为0,
        dp[..][0]目标为0,则方法数为1

3. 转移方程：
        dp[i][j] = dp[i-1][j]               +            dp[i][j-coins[i-1]]
        两种情况组成
                    1. 不选择第i个物品，那么dp[i][j] == dp[i-1][j]
                        从前i-1个硬币中挑选，组成目标为j
                    2. 选择第i个物品，那么dp[i][j] == dp[i][j - coins[i-1]]从前i个硬币中挑选，组成目标为j-coins[i-1]，
                                            之所以i-1是因为，i=0表示没有硬币可以挑选，而非选择第一个

        上面方程需要满足条件 j - coins[i-1] >= 0

        otherwise
        dp[i][j] = dp[i-1][j]

4. 返回dp[-1][-1]

优化空间复杂度：
使用一行就行，代表目标
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 特殊情况
        if amount == 0:
            return 1
        if not coins:
            return 0

        # 初始化数组
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        # 动态转移
        # 金币
        for i in range(1, n + 1):
            # 目标
            for j in range(1, amount + 1):

                if j - coins[i - 1] < 0:
                    # 不选硬币coins[i-1], 从前i-1个金币选，凑目标j
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 选硬币coins[i-1], 从前i个金币选，凑目标j
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[-1][-1]




"""
优化空间复杂度
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 特殊情况
        if amount == 0:
            return 1
        if not coins:
            return 0

        # 初始化数组
        n = len(coins)
        # dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp = [0 for _ in range(amount + 1)]

        # for i in range(n + 1):
        # dp[i][0] = 1
        dp[0] = 1

        # 动态转移
        # 金币
        for i in range(1, n + 1):
            # 目标
            for j in range(1, amount + 1):

                if j - coins[i - 1] < 0:
                    # 不选硬币coins[i-1], 从前i-1个金币选，凑目标j
                    # dp[i][j] = dp[i - 1][j]
                    dp[j] = dp[j]
                else:
                    # 选硬币coins[i-1], 从前i个金币选，凑目标j
                    # dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                    dp[j] = dp[j] + dp[j - coins[i - 1]]
        return dp[-1]