"""
定义状态：dp[i][k][0/1]第i天，当前进行了k次买入，当前0不持有股票，或者1持有股票
状态转移方程：dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                                保持不变        卖出

            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
                                保持不变        买入，所以交易次数加1

base case:
            dp[0][][0] = 0;  第0天，利润为0
            dp[][0][] = 0   当前没有进行交易，利润为0
            dp[0][][1] = -prices[0]

结论：我们想要在最后一天并不持有股票，这样利润才会最大。因此dp[i][k][0]是我们想要的，至于dp[i][k][1]是为了计算dp[][][0]
对于只允许一次交易的k=1
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
                                保持不变        卖出
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
                                保持不变        买入，所以交易次数加1

可以将k所在维度消去

base case:
            dp[0][1] = - prices[0]
            dp[0][0] = 0
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. 特殊情况
        if not prices:
            return 0

        # 2. 初始化dptable
        n = len(prices)  # 天数
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # 第1天，买入，为负
        dp[0][1] = -prices[0]
        # 3. 动态转移
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[n - 1][0]


"""
进一步优化动态转移数组的空间复杂度为1
我们观察发现，转移方程只与前一天和后一天有关
dp_i1_0 = max(dp_i1_0, dp_i1_1+prices[i])

dp_i1_1 = max(dp_i1_1, -prices[i])

base case: dp[0][1] = -prices[0] dp[0][0] = 0
        dp_i1_0 = 0; dp_i1_1 = -prices[0]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. 特殊情况
        if not prices:
            return 0

        # 2. 初始化dptable
        n = len(prices)  # 天数
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        # 3. 动态转移
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0