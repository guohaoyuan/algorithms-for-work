"""
因为相邻两个不能被偷，妖魔偷窃范围[0, n-2]，妖魔偷窃范围[1, n-1], 妖魔偷窃范围[1, n-2]
                        len     n-1             n-1                 n-2

所以我们只需考虑前两种情况，因为偷窃范围更广

定义状态：
        dp[i]表示第i个位置，我们偷或者不偷，所获得的财产

转移方程：
        倒着计算, 可以避免重复子问题
        dp[i] = max(dp[i+1], dp[i+2] + nums[i])


优化空间复杂度：
        dp_i = max(dp_i_1, dp_i_2+nums[i])
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i

base case:
        dp[n] = dp[n+1] = 0

"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_range(start, end):
            # 初始化base case
            dp_i_1 = dp_i_2 = 0

            for i in range(end, start - 1, -1):
                dp_i = max(dp_i_1, dp_i_2 + nums[i])
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i

            return dp_i

        if not nums:
            return 0

        n = len(nums)

        # 必须考虑长度只有1，否则rob_range回报错，因为没有进入for循环
        if n == 1:
            return nums[0]

        return max(rob_range(0, n - 2), rob_range(1, n - 1))
