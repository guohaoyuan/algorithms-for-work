# -*- coding : utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划：
        动态转移方程：dp[i] = dp[i - 1] + nums[i], if dp[i-1]>=0因为其对求和其促进作用；
                            nums[i]，if dp[i-1]<0，因为其对求和起反作用
        初始状态：dp[0] = nums[0]
        :param nums:
        :return:
        """

        # 1. 特殊情况数组为空
        if not nums:
            return 0

        # 2. 初始化变量
        dp = nums
        # 此时原地修改相当于已经求得初始状态

        # 3. 算法流程
        for i in range(1, len(nums)):
            if dp[i -1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

    # 不修改原输入
    def maxSubArray_v2(self, nums):
        # 1. 特殊情况：输入为空
        if not nums:
            return 0

        # 2. 定义状态转移方程的初始状态
        max_dp = nums[0]
        dp = nums[0]

        # 3. 动态转移方程从第二位开始
        for i in range(1, len(nums)):
            if dp >= 0:
                dp = dp + nums[i]
            else:   # 如果dp<0，此时相加反而比nums[i]更小了
                dp = nums[i]
            max_dp = max(max_dp, dp)
        return max_dp

if __name__ == '__main__':
    test1 = [-2,1,-3,4,-1,2,1,-5,4]
    test2 = list(test1)
    solution = Solution()
    print(solution.maxSubArray(test1))
    print(solution.maxSubArray_v2(test2))
    """
    时间复杂度：n,遍历一次数组
    空间复杂度：1,原地修改。如果不允许原地修改，n创建辅助数组
    """