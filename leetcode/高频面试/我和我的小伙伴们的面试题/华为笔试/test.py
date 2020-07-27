# -*- coding : utf-8 -*-

"""
最少硬币问题
"""

class Solution:
    def coinChange(self, coins, amount, coins_num):
        """

        :param coins: list
        :param amount: int
        :return: int
        """
        res = 0
        for i in range(len(coins) - 1, -1, -1):
            tmp = min(amount // coins[i], coins_num[i])
            res += tmp
            amount -= tmp * coins[i]
        return res

    def coinChange_v2(self, coins, amount, coins_num):
        """

        :param coins: list
        :param amount: int
        :return: int
        """
        # 硬币面值数
        n = len(coins)

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        print(dp)

        for i in range(n):  # 挨个遍历硬币
            for j in range(1, coins_num[i] + 1):    # 挨个遍历硬币数目
                # for k in range(amount, coins[i] - 1, -1):   # 目标到面值
                #     dp[k] = min(dp[k], dp[k - coins[i]] + 1)
                for k in range(1, amount + 1):
                    if k - coins[i] < 0:
                        continue
                    dp[k] = min(dp[k], dp[k - coins[i]] + 1)

        return dp[-1] if dp[-1] != amount + 1 else -1

if __name__ == "__main__":
    coins1 = [1, 2, 5]
    amount1 = 18
    coins1_num = [3, 3, 3]
    coins = [1, 3, 7, 11, 13]
    coins_num = [1, 2, 3, 4, 1]
    amount = 30
    solution = Solution()
    print(solution.coinChange(coins1, amount1, coins1_num))
    print(solution.coinChange_v2(coins, amount, coins_num))
    """
    时间复杂度：nk
    空间复杂度：k
    """