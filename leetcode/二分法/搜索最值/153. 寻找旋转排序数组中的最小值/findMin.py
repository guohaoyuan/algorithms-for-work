"""本题要求不能有重复元素"""


class Solution:
    def findMin(self, nums):
        # 1. 特殊情况: 数组为空直接返回
        if not nums:
            return

        # 2. 初始化左右指针
        L, R = 0, len(nums) - 1

        # 3. 二分法
        # while L <= R:
        #     mid = (L + R) // 2
        #
        #     # 左右边界相等时直接返回
        #     if nums[L] <= nums[R]:
        #         return nums[L]
        #     # 我们需要判断前段是否有序
        #     # 如果前段有序,则最小元素在后端
        #     # 如果前段无序,则最小元素在前段
        #     if nums[R] <= nums[mid]:    # 两者有可能相等, 当数组长度为1 或 2
        #         # 最小元素所在区间(mid, R]
        #         L = mid + 1
        #     elif nums[L] > nums[mid]:                       #
        #         # 最小元素所在区间(L, mid]
        #         R = mid
        # # 搜索完成自然是最小
        # # return

        while L <= R:
            mid = (L + R) // 2

            if L == R:
                return nums[mid]

            if nums[mid] < nums[R]: # 则最小值在[L, mid]
                R = mid
            elif nums[mid] > nums[R]:   # 最小值在(mid, R]
                L = mid + 1
            elif nums[mid] == nums[R]:  # 最小值在mid,
                # if L == R:              # 此时三点收敛
                #     print(True)
                return nums[mid]


if __name__ == "__main__":
    nums1 = [3,4,5,1,2]
    nums2 = [4,5,6,7,0,1,2]
    solution = Solution()
    print(solution.findMin(nums1))
    print(solution.findMin(nums2))