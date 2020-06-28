class Solution:
    def search(self, nums, target):
        # 1. 特殊情况:如果数组为空,则返回F
        if not nums:
            return False

        # 2. 初始化左右边界
        L, R = 0, len(nums) - 1

        # 3. 二分法
        while L < R:
            mid = (L + R) // 2

            if target == nums[mid]:
                return True
            elif target != nums[mid]:
                if nums[mid] < nums[R]: # 右边有序,
                    if nums[mid] < target <= nums[R]:
                        # 目标在右侧, 搜索区间(mid, R]
                        L = mid + 1
                    else:
                        # 目标在左侧,搜索区间[L, mid)
                        R = mid - 1
                elif nums[mid] > nums[R]:   # 左边有序
                    if nums[L] <= target < nums[mid]:
                        # 目标在左侧,搜索区间[L, mid)
                        R = mid - 1
                    else:
                        # 目标在右侧,搜索区间(mid, R]
                        L = L + 1
                elif nums[mid] == nums[R]:
                    R = R - 1
                    # 可以遇到下一个元素
        return False if nums[L] != target else True  # 三点收敛


def search(nums, target):
    if not nums:
        return False

    n = len(nums)

    L, R = 0, n - 1

    while L <= R:
        mid = (L + R) // 2

        if L == R:
            if nums[L] == target:
                return True
            else:
                return False

        if nums[mid] == target:
            return True
        elif nums[mid] != target:
            if nums[mid] < nums[R]:
                if nums[mid] < target <= nums[R]:
                    # (mid, R)
                    L = mid + 1
                else:
                    R = mid - 1
            elif nums[mid] > nums[R]:

                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            elif nums[mid] == nums[R]:
                R -= 1
    return False


if __name__ == "__main__":
    nums1 = [2, 5, 6, 0, 0, 1, 2]
    target1 = 0
    target2 = 3
    solution = Solution()
    print(solution.search(nums1, target1))
    print(solution.search(nums1, target2))