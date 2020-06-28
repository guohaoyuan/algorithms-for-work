"""
执行两次二分法,第一次遇到target时, 收缩右边界, R = mid - 1, 找到右边界
             第二次遇到target是, 收缩左边界, L = mid + 1, 找到左边界
"""


class Solution:

    def searchRange(self, nums, target):
        # 1. 特殊情况: 数组为空
        if not nums:
            return [-1, -1]

        # 2. 初始化左右边界
        L, R = 0, len(nums) - 1

        # 3. 第一次二分法,找到右边界
        while L <= R:
            mid = (L + R) // 2
            # print(L, R)
            if nums[mid] > target:
                # 目标在左侧,搜索区间[L, mid)
                R = mid - 1
            elif nums[mid] < target:
                # 目标在右侧, 搜索区间(mid, R]
                L = mid + 1
            elif nums[mid] == target:
                # 先找右边界
                L = mid + 1

        #

        right = L - 1

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            # print(L, R)

            if nums[mid] > target:
                # 搜索区间[L, mid)
                R = mid - 1
            elif nums[mid] < target:
                # 搜索区间(mid, R]
                L = mid + 1
            elif nums[mid] == target:
                # 找到左边界
                R = mid - 1


        left = R + 1

        return [left, right] if left <= right else [-1, -1]


if __name__ == '__main__':
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    target2 = 6
    nums2 = [2, 2]
    target3 = 1
    solution = Solution()
    print(solution.searchRange(nums1, target1))
    print(solution.searchRange(nums1, target2))
    print(solution.searchRange(nums2, target3))