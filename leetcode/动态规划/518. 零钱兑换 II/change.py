class Solution:

    def change(self, amount, coins):
        # 1. 特殊情况:如果目标金额为0,直接返回1,

        # 2. 初始化动态数组
        m = len(coins)
        n = amount
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        for i in range(m + 1):
            dp[i][0] = 1

        # 3. 动态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i-1][j]
                # print(dp)
        return dp[-1][-1]

    def change_v2(self, amount, coins):
        """
        我们观察动态转移表,发现只与上一层相关
        所以我们只使用上一
        """

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1 # 表示当目标为0,只需要1种方法就行,其实也是为了凑出结果

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]
                else:
                    dp[j] = dp[j]
        return dp[-1]

if __name__ == "__main__":
    amount1 = 5
    coins1 = [1, 2, 5]
    solution = Solution()
    print(solution.change(amount1, coins1))
    """
    时间复杂度: n*m
    空间复杂度: n *m
    """
    print(solution.change_v2(amount1, coins1))