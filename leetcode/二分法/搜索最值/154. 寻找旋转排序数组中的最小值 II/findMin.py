class Solution:

    def findMin(self, nums):
        # 1. 特殊情况: 数组为空,直接返回
        if not nums:
            return

        # 2. 初始化左右边界
        L, R = 0, len(nums) - 1

        # 3. 二分法
        while L <= R:
            mid = (L + R) // 2

            if L == R:
                return nums[L]

            if nums[mid] < nums[R]: # 最小值一定在区间[L, mid]上
                R = mid
            elif nums[mid] > nums[R]:   # 最小值一定在区间(mid, R]上
                L = mid + 1
            elif nums[mid] == nums[R]:  # 不能确定当前mid在左侧还是右侧,我们直接减少R
                R = R - 1
                # R 自减不会越过最小值；具体说,如果R是最小值,那一定不是唯一最小值,不担心越过；如果不是最小值,等遇到最小值,则不满足该条件

