# -*- coding = utf-8 -*-

class Solution(object):

    def maxSubArray(self, nums):
        """
        容易想到暴力解法，需要两重嵌套循环，时间复杂度n方，不能满足需要，我们考虑动态规划
        :param nums: 数组无序，有正数，也有负数
        :return: 返回int表示有连续子数组的和
        """
        # 1. 特殊情况不存在

        # 2. 初始化dp
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i - 1] >= 0:
                dp[i] = dp[i-1] + nums[i]
                # print(dp)
            else:
                dp[i] = nums[i]
        return max(dp)
        '''
        时间复杂度：n，遍历一次列表
        空间复杂度：n
        '''

    def maxSubArray1(self, nums):
        """
        此处将利用动态规划，优化空间复杂度，原地修改
        :param nums:
        :return:
        """
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                nums[i] = nums[i - 1] + nums[i]
            else:
                # nums[i] = nums[i]
                continue
        return max(nums)
        '''
        时间复杂度：n
        空间复杂度：1
        '''

if __name__ == '__main__':
    test1 = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(test1))
    print(solution.maxSubArray1(test1))