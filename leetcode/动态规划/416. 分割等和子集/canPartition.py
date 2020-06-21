class Solution:
    def canPartition(self, nums):
        # 1. 初始化动态数组
        # 行数为选择物品
        m = len(nums)
        # 列数
        n = sum(nums) / 2

        # 如果和不为整数直接返回F,因为nums都是正整数
        if int(n) != n:
            return False
        n = int(n)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = True

        # 动态转移方程,外层为物品,内层为目标
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
if __name__ == "__main__":
    nums1 = [1, 5, 11, 5]
    nums2 = [1, 2, 3, 5]
    solution = Solution()
    print(solution.canPartition(nums1))
    print(solution.canPartition(nums2))