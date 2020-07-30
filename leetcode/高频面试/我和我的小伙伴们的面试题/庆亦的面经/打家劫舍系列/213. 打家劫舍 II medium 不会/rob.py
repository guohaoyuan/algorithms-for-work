"""
此时，有三种偷窃范围，
            [0, n-2] : 不偷末尾元素 1, 2, 3 偷3，范围n-2 + 1=n-1
            [1, n-1] : 不偷末尾元素 1, 2, 3 偷1，范围n-1-1+1=n-1
            [1, n-2] : 不偷首尾元素 1, 2, 3 偷2，范围n-2-1+1=n-2
明显偷窃范围更大一些好

1. 定义状态：dp[i]表示到达当前位置，所能偷到的金额

2. 定义方法同打家劫舍1

3. 返回最大的即可
"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        def helper(nums):
            dp_2 = nums[0]
            dp_1 = max(nums[0], nums[1])
            n = len(nums)
            for i in range(2, n):
                dp_i = max(dp_1, dp_2 + nums[i])
                dp_2 = dp_1
                dp_1 = dp_i
            return dp_1

        # 在指定范围内遍历
        res1 = helper(nums[1:])
        res2 = helper(nums[:-1])
        return max(res1, res2)