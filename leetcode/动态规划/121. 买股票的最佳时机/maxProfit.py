# -*- coding : utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        动态规划：
        状态转移方程:
        dp(i) = max(dp(i-1), prices[i] - min(prices[:i), prices[i])
        :param prices:
        :return:
        """
        # 1. 特殊情况：数组为空
        if not prices:
            return 0

        # 2. 初始化变量：minPrices 表示前i - 1天最小价格；dp表示当前最大利润。cost表示第二项
        # cost = 0
        minPrices = prices[0]
        dp = 0

        # 3. 算法流程：
        for i in range(1, len(prices)):
            if minPrices > prices[i]:   # 更新最小值
                minPrices = prices[i]

            cost = prices[i] - minPrices
            dp = max(dp, cost)
        return dp

if __name__ == '__main__':
    test1 = [7,1,5,3,6,4]
    test2 = [7,6,4,3,1]
    solution = Solution()
    print(solution.maxProfit(test1))
    print(solution.maxProfit(test2))
    """
    时间复杂度：n，遍历一次数组
    空间复杂度：1,只用了常数级别变量
    """