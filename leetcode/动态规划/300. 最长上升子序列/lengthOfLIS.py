# -*- coding : utg-8 -*-

class Solution:
    def lengthOfLIS(self, nums):
        """
        固定i
            看[0,i]区间
                如果nums[i]>nums[j],dp[i] = max(dp[i], dp[i] + 1)
        取最大
        :param nums: list
        :return: int
        """

        # 1. 特殊情况：数组长度<2
        n = len(nums)

        if n < 2:
            return n

        # 2. 初始化动态数组，长度为n，初始化为1,dp[0]=1
        dp = [1 for _ in range(n)]

        # 3. 算法流程：
        # 动态转移方程  dp[i] = max(dp[j] + 1, dp[i]) if 0 <= j < i and nums[j] < nums[i]
        for i in range(1, n):   # 遍历nums
            for j in range(i):  # 遍历dp
                if j < i and nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        res = max(dp)
        return res

    def lengthOfLIS_v2(self, nums):
        """
        利用贪心算法+二分查找
        整体思路，
        创建一个cell的列表，用于保存最长上升子序列
        遍历数组
            如果当前元素大于最后一个位置的元素，则插入cell
            否则，利用二分查找，将当前元素插入cell中，大于等于当前元素中最小元素的位置

        :param nums:
        :return:
        """
        # 1. 特殊情况：数组长度小于2
        n = len(nums)
        if n < 2:
            return n

        # 2. 初始化cell
        cell = []

        # 3. 算法流程
        for num in nums:
            if not cell or num > cell[-1]:
                cell.append(num)
            else:
                # 初始化左右指针L R
                L, R = 0, len(cell) - 1
                while L < R:    # 此时没有让两者相等
                    mid = (L + R) // 2
                    if cell[mid] < num:
                        L = mid + 1
                    else:   # cell[mid] >= num
                        R = mid
                # 找到对应位置，覆盖掉原来的元素
                cell[L] = num
        return len(cell)

if __name__ == "__main__":
    nums1 = [10,9,2,5,3,7,101,18]
    solution = Solution()
    print(solution.lengthOfLIS(nums1))
    nums1 = [10,9,2,5,3,7,101,18]
    print(solution.lengthOfLIS_v2(nums1))
    """
    动态规划：如果在面试时，举例1, 2, 3, 4, 0
    f(0) = 0 + 1 = 1
    f(1) = max(f(0) + 1, 0 + 1) = 2
    f(2) = max(f(0) + 1, f(1) + 1, 0 + 1) = 3
    f(3) = max(f(0) + 1, f(1) + 1, f(2) + 1, 0 + 1) = 4
    f(4) = max(f(0) + 1, f(1) + 1, f(2) + 1, f(3) + 1) = 1
    所以还要取最大
    
    时间复杂度：n^2
    空间复杂度：n
    
    
    贪心策略+二分查找
    核心思想是利用cell存储较小的元素，
    时间复杂度：nlogn
    空间复杂度：n
    """