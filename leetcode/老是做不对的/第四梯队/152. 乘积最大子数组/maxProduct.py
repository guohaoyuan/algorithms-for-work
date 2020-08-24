"""
1. 初始化用两个变量来表示当前的最大值和最小值imax, imin
    初始化res用于返回最大值
2. 由于遇到负数会两级翻转，所在以遇到负数交换imax, imin
3. 更新最大值和最小值imax, imin
4. 返回最大值res
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return

        res = - float('inf')
        imin, imax = 1, 1

        for i in range(len(nums)):
            if nums[i] < 0:
                imin, imax = imax, imin

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(res, imax)
        return res