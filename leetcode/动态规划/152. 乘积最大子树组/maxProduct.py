# -*- coding : utf-8 -*-

class Solution:
    def maxProduct(self, nums):
        """

        :param nums: list
        :return: int
        """
        # 1. 特殊情况：数组为空，
        if not nums:
            return 0

        # 2. 初始状态
        Max = - 1 << 31
        imax = 1
        imin = 1

        # 3. 算法流程
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            Max = max(Max, imax)
        return Max

if __name__ == '__main__':
    nums1 = [2, 3, -2, 4]
    nums2 = [-2, 0, -1]
    solution = Solution()
    print(solution.maxProduct(nums1))
    print(solution.maxProduct(nums2))