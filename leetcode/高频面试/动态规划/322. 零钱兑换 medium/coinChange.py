"""

"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0

        m = len(coins)
        n = amount

        dp = [[0 for _ in range(amount + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            dp[0][i] = -1

        for i in range(1, m + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
        return dp[-1][-1]