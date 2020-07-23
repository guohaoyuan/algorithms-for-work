"""
定义状态：
        dp[i]表示选择前i个硬币所需要的最少硬币数

定义转移方程：
        dp[i] = min(dp[i], dp[j-coin] + 1) if j - coin >=0
                continue
base case:
        dp[0] = 0

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for j in range(1, amount + 1):
                if j - coin >= 0:
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1