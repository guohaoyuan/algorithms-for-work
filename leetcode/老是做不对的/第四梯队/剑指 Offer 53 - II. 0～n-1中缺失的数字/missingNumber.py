"""

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return

        L, R = 0, len(nums)
        while L <= R:
            if L == R:
                return L
            mid = (L + R) >> 1
            if nums[mid] == mid:
                # 搜索区间在右侧
                L = mid + 1
            elif nums[mid] > mid:
                # 搜索区间
                R = mid
            # elif nums[mid] < mid:
