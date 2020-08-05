"""
1. 定义状态dp[i]表示n解台阶的方法数

2. 定义转移方程dp[i] = dp[i-1]   +    dp[i-2]
                    迈一个台阶             迈两个台阶

3. base case dp[0] = 0 dp[1] = 1 dp[2] = 2
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]



"""
优化空间结构
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        # dp = [0 for _ in range(n + 1)]
        dp_1 = 1
        dp_2 = 2

        for i in range(3, n + 1):
            dp_i = dp_1 + dp_2
            dp_1, dp_2 = dp_2, dp_i

        return dp_i