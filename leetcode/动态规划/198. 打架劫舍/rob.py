# -*- coding : utf-8 -*-

class Solution:
    def rob(self, nums):
        """
        动态规划：
        dp[i]表示前i个房子，偷得的最大金额
        当我们选择偷第i个房子时，我们就不能偷i-1,dp[i-2] + nums[i]
        当我们选择不偷第i个房子时，得到是前i-1个房子最大金额 dp[i-1]
        我们要选择两者中最大的作为偷前i个房子的金额
        dp[i] =  max(dp[i-2], nums[i], dp[i-1])

        :param nums:
        :return:
        """
        # 1. 特殊情况：数组为空
        if not nums:
            return

        n = len(nums)

        # 2. 初始状态
        one = nums[0]
        if n == 1:
            return one

        two = max(nums[1], nums[0])
        if n == 2:
            return two

        # 3. 动态转移
        for i in range(2, n):
            three = max(two, one + nums[i])
            one = two
            two = three
        return three

if __name__ == "__main__":
    test1 = [1, 2, 3, 1]
    test2 = [2, 7, 9, 3, 1]

    solution = Solution()
    print(solution.rob(test1))
    print(solution.rob(test2))