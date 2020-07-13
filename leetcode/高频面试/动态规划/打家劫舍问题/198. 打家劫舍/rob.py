"""
定义状态:
        dp[i]表示出发位置为i，我们可以选择偷还是不偷，得到的财产

转移方程：
        dp[i] = max(dp[i+1],            dp[i+2] + nums[i])
                表示不偷，去下一个位置;    表示偷，偷去下下一个位置

优化空间复杂度
        dp_i = max(dp_i_1, dp_i_2 + nums[i])

base case:
        我们倒着向前看，这样可以避免重复子问题
        dp[n] = 0   ---> dp_i_1 = 0
        dp[n+1] = 0 ---> dp_i_2 = 0
        创建数组长度为n+2

"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp_i_1 = dp_i_2 = 0

        for i in range(n - 1, -1, -1):

            dp_i = max(dp_i_1, dp_i_2 + nums[i])
            # 更新两个变量
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i