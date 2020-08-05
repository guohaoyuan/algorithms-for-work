"""
寻找峰值，一个比较有用的算法，一定要会

我们比较numd[mid] nums[mid+1]
分三种情况：
        一种是降序的情况，这样搜索区间变为[L, mid]
        一种是升序的情况，这样搜索区间变为[mid + 1, R]
        一种是相等的情况，其实这个情况不存在

我就是奇怪为什么mid + 1 不担心越界
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return

        n = len(nums)
        L, R = 0, n - 1

        while L <= R:
            mid = (L + R) >> 1
            if L == R:
                return L
            if nums[mid] == nums[mid + 1]:
                # 搜索区间[mid + 1, R]
                L = mid + 1
            elif nums[mid] < nums[mid + 1]:
                # 搜索区间[mid + 1, R]
                L = mid + 1
            elif nums[mid] > nums[mid + 1]:
                # 搜索区间[L, mid]
                R = mid
