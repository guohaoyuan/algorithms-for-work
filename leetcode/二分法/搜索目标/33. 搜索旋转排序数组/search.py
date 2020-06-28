class Solution:

    def search(self, nums, target):
        """

        :param nums: list
        :param target: int
        :return:
        """
        # 1. 特殊情况: 数组为空,返回-1
        n = len(nums)
        if n == 0:
            return -1

        # 2. 初始化左右边界
        L = 0
        R = n - 1

        # 3. 二分查找
        # 首先根据nums[mid]和nums[0]的关系,判断前半端有序还是后半段有序
        # while L <= R:
        #     mid = (L + R) // 2
        #     if target == nums[mid]: # 找到目标
        #         return mid
        #     elif nums[L] <= nums[mid]:       # 左侧连续, 因为mid可能==L,所以此处用等号
        #         if nums[L] <= target < nums[mid]:   # target在左侧,搜索区间[L, mid)
        #             # 更新右边界, 肯定不含mid
        #             R = mid - 1
        #         else:                               # target在右侧,搜索区间(mid, R]
        #             L = mid + 1
        #     elif nums[R] > nums[mid]:       # 右侧连续
        #         if nums[mid] < target <= nums[R]:   # target在右侧,搜索区间(mid, R]
        #             L = mid + 1
        #         else:                               # target在左侧, 搜索区间[L, mid)
        #             R = mid - 1
        # return -1

        while L <= R:
            mid = (L + R) // 2
            # 有搜索目标的,不同于找最小值的题
            if target == nums[mid]:
                return mid
            elif target != nums[mid]:
                if nums[mid] < nums[R]: # 右边有序,
                    if nums[mid] < target <= nums[R]:    # 目标在右边,搜索区间(mid, R]
                        L = mid + 1
                    else:                                # 目标在左边,搜索区间[L, mid)
                        R = mid - 1
                elif nums[mid] > nums[R]:   # 左边有序
                    if nums[L] <= target < nums[mid]:   # 目标在左边,搜索 区间[L, mid)
                        R = mid - 1
                    else:                               # 目标在右边,搜索区间(mid, R]
                        L = mid + 1
                elif nums[mid] == nums[R]:              # 不存在重复元素,此时三点收敛,
                    # 但是却不是目标
                    return -1 



def search(nums, target):
    if not nums:
        return -1
    n = len(nums)
    L, R = 0, n - 1

    while L <= R:

        mid = (L + R) // 2

        if L == R:
            if nums[L] != target:
                return -1

        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < nums[R]:
                if nums[mid] < target <= nums[R]:
                    # (mid, R]
                    L = mid + 1
                else:
                    # (L, mid)
                    R = mid - 1

            elif nums[mid] > nums[R]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
    # print(L, R)
    return -1


if __name__ == "__main__":
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    solution = Solution()
    # print(solution.search(nums1, target1))
    # print(solution.search(nums2, target2))
    nums3 = [1, 3]
    target3 = 0
    print(search(nums3, target3))