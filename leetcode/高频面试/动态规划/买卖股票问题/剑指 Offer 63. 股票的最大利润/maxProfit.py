class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0