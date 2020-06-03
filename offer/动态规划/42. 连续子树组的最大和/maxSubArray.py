# -*- coding = utf-8 -*-

class Solution(object):

    def maxSubArray(self, nums):
        """
        动态规划：dp(n) = dp(n-1) + nums[i] ,此时dp[n-1] >=0,因为此时对于数组的结果起到正作用;
                        nums[i]，此时dp[n-1] < 0，因为此时对于数组的结果起反作用，重新初始化dp
        :param nums:
        :return:
        """
        # 1. 特殊情况：数组为空
        n = len(nums)
        if n == 0:
            return

        # 2. 初始化：dp，如果可以原地修改直接使用原数组
        dp = nums

        # 3. 算法流程：更新dp
        for i in range(1, n):   # 当n ==1时，就不执行循环，直接返回结果
            if dp[i - 1] >= 0:  # 这个等号在哪里其实影响不大
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

if __name__ == '__main__':
    test1 = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(test1))
    """
    时间复杂度：n，遍历一次数组更新数组+求数组最大值，都是n时间复杂度
    空间复杂度：如果允许原地修改则是1；否则创建辅助数组为n
    """