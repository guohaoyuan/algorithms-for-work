# -*- coding : utf-8 -*-

class Solution:
    def coinChange(self, coins, amount):
        """

        :param coins: list
        :param amount: int
        :return: int
        """
        # 1. 特殊情况：数组为空
        if not coins:
            return 0

        # 2. 初始化动态转移数组，长度为n+1，第一个位置为空，初始化为无穷大，用amount+1代替
        # dp[0]=0
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        # 3. 算法流程
        # 外层循环遍历dp数组

        for coin in coins:  # 内层遍历硬币数
            for i in range(1, amount + 1):
                if i - coin < 0:    # 此时直接看下一个硬币
                    continue
                # 利用动态转移方程
                print(dp)
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == amount + 1 else dp[-1]

if __name__ == "__main__":
    coins1 = [1, 2, 5]
    amount1 = 11
    coins2 = [2]
    amount2 = 3
    solution = Solution()
    print(solution.coinChange(coins1, amount1))
    print(solution.coinChange(coins2, amount2))
    """
    时间复杂度：nk
    空间复杂度：k
    """