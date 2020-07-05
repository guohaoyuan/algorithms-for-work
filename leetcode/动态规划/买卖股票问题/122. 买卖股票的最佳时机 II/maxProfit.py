"""
定义状态： dp[i][k][0/1] 表示第i天，买入k次，持有股票/不持有股票的利润

转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] +prices[i])
                    保持              卖出

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                    保持              买入，买入次数加1

由于买入次数不限制， k = 正无穷， 则k==k-1

动态转移方程：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                保持          卖出

dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
                保持          卖出

base case:
dp[0][0] = 0
dp[0][1] = - prices[0]



"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # base case
        dp_i_0 = 0
        dp_i_1 = - prices[0]

        # dp table
        for i in range(1, n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0