class Solution:

    def findDuplicate(self, nums):
        # 1. 特殊情况: 如果数组为空, 返回
        if not nums:
            return

        # 2. 初始化左右边界
        n = len(nums)
        L = 1   # 初始位置应该是范围,不是索引
        R = n - 1

        # 3. 二分法
        # 首先有一个统计次数的函数
        def helper(start_num, end_num, nums):
            # 初始化区间上的统计次数
            count = 0

            for num in nums:
                # 在[start_num, end_num]之间数字出现的次数
                if start_num <= num <= end_num:
                    count += 1
                else:
                    continue
            return count

        while L <= R:
            mid = (L + R) // 2

            # 左侧的数字数目
            left = helper(L, mid, nums)
            if left > mid - L + 1:    # 左侧数字多于右侧
                # 搜索区间为[L, mid]
                R = mid
            elif left <= mid - L + 1:  # 右侧数字多于左侧
                # 搜索区间为(mid, R]
                L = mid + 1

            if L == R:
                # 三值相聚
                return L

if __name__ == '__main__':
    nums1 = [1,3,4,2,2]
    nums2 = [3,1,3,4,2]

    solution = Solution()
    print(solution.findDuplicate(nums1))
    print(solution.findDuplicate(nums2))
    """
    时间复杂度:nlogn
    空间复杂度:1
    不过有一点要注意,如果数组中有多个重复数字,可能找不出来所有的数字
    """