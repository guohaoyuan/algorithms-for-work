"""
执行两次二分查找,
第一次二分查找,
    nums[mid] == target: 更新左边界L = mid + 1
第二次二分查找,
    nums[mid] == target: 更新右边界R = mid - 1
最终得到 L - R + 1

"""

class Solution:
    def search(self, nums, target):
        # 1. 特殊情况: 数组为空,返回0
        if not nums:
            return 0

        # 2, 初始化左右边界LR
        L, R = 0, len(nums) - 1

        # 3. 二分法查找
        while L <= R:
            mid = (L + R) // 2

            if nums[mid] > target:
                # 则目标在左侧, 搜索区间[L, mid)
                R = mid - 1
            elif nums[mid] < target:
                # 目标在右侧, 搜索区间(mid, R]
                L = mid + 1
            elif nums[mid] == target:
                # 需要先找到右边界
                L = mid + 1
        # 当三点收敛时,L位于target的左边第一个元素

        left = L

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2

            if nums[mid] > target:
                # 目标在左边,搜索区间[L, mid)
                R = mid - 1
            elif nums[mid] < target:
                # 目标在右边,搜索区间(mid, R]
                L = mid + 1
            elif nums[mid] == target:
                # 需要找到左边界
                R = mid - 1
        # 三点收敛时, R位于target的右边第一个元素
        right = R
        print(left, right)
        return left - right - 1


def search(nums, target):
    if not nums:
        return 0

    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        elif nums[mid] == target:
            L = mid + 1

    right = L - 1

    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        elif nums[mid] == target:
            R = mid - 1

    left = R + 1

    return (right - left + 1) if right - left >= 0 else 0


if __name__ == "__main__":
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    target2 = 6
    target3 = 1
    nums3 = [1]
    solution = Solution()
    print(solution.search(nums1, target1))
    print(solution.search(nums1, target2))
    print(solution.search(nums3, target3))