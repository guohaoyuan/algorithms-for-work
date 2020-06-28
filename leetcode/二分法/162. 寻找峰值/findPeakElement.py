"""
思路,二分法,

1. 确定左右边界
L, R

2. 如果mid < mid +1位置的数,说明它处于局部上升, 更新区间(mid + 1, R]

3. 如果mid > mid + 1位置的数,说明它处于局部下降. 更新区间[L, mid]

"""

class Solution:

    def findPeakElement(self, nums):
        # 1. 特殊情况:数组为空 ,直接返回
        if not nums:
            return
        #
        # 2. 初始化数组长度 L R
        n = len(nums)
        # if n == 1:
        #     return 0
        L, R = 0, n - 1

        # 3. 二分法
        while L <= R:
            mid = (L + R) // 2
            if L == R:
                # 三值聚合
                return L
            if nums[mid] > nums[mid + 1]:
                # 局部下降,搜索区间[L, mid]
                R = mid
            elif nums[mid] < nums[mid + 1]:
                # 局部上升, 搜索区间(mid, R]
                L = mid + 1
            elif nums[mid] == nums[mid + 1]:
                L = mid + 1 # 我这是随意找的,



if __name__ == '__main__':
    nums1 = [1,2,3,1]
    nums2 = [1,2,1,3,5,6,4]
    solution = Solution()
    print(solution.findPeakElement(nums1))
    print(solution.findPeakElement(nums2))