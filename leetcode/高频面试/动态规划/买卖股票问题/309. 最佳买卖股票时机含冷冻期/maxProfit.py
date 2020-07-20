"""
状态定义
    dp[i][k][0/1] 第i天买入k次，持有股票/不持有股票的利润

状态转移方程：
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                        保持          卖出

    dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k-1][0] - prices[i])
                        保持          买入，表示我们第i天选择买入，则前一天为冷冻期，此期间无任何买入卖出操作，前前一天不是冷冻期

优化空间复杂度：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

    dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

    对于dp[i-2][0]， 当i=1, i-2不存在，初始化dp[-i-2][0]也为0
base case:
    dp[0][0] = 0
    dp[0][1] = - prices[0]

小细节：
    更新dp[i-2][0]的状态，即dp_i_prev

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if n > 1:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])      # 判断语句不用加，因为一开始dp[-1][0]=0
        return dp[-1][0]



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        dp_i_0 = 0
        dp_i_1 = - prices[0]
        dp_i_prev = 0

        for i in range(1, n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_prev - prices[i])
            # 更新dp_i_prev
            dp_i_prev = tmp
        return dp_i_0