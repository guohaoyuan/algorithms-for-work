# -*- coding : utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        首先想到暴力解法，固定当前天，遍历后面的天，时间复杂度n**2
        优化：我们考虑动态规划
        转移方程dp[i] = max(dp[i-1], nums[i] - min(nums[:i+1]))
        :param prices:
        :return:
        """
        # 1. 特殊情况：不足两天利润为0
        n = len(prices)
        # if n < 2:
        #     return 0

        # 2. 初始化方程初始状态：
        dp = 0 # 第1天利润
        cost = prices[0] # 第1天最小成本

        # 3. 算法流程
        for i in range(1, n):
            cost = min(cost, prices[i])
            dp = max(dp, prices[i] - cost)
        return dp
if __name__ == '__main__':
    test1 = [7,1,5,3,6,4]
    test2 = [7,6,4,3,1]
    solution = Solution()
    print(solution.maxProfit(test1))
    print(solution.maxProfit(test2))
    """
    时间复杂度：n，遍历一次数组
    空间复杂度：1,常数级别的变量
    """