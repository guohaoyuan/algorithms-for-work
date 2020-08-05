"""
1. 定义状态：dp[i]表示到达当前位置所能偷到的钱

2. 动态转移方程： dp[i] = max(dp[i-2] + nums[i],                   dp[i-1])
                        选择偷当前位置，所以前一个位置不能偷     不偷当前位置，所以保持前一个位置的金额

3. base case: dp[0] = nums[0]

优化空间复杂度：

"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        if n <= 2:
            return max(nums)

        # dp_2表示-2天的最大金额
        dp_2 = nums[0]
        dp_1 = max(nums[0], nums[1])

        for i in range(2, n):
            dp_i = max(dp_1, dp_2 + nums[i])
            dp_2 = dp_1
            dp_1 = dp_i
        return dp_i