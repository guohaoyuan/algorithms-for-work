"""
要求时间复杂度为n

输入是一个无序的数组，要求有序输出
"""

class Solution:

    def sort(self, nums, n):
        # 1. 特殊情况：数组为空
        if not nums:
            return []

        # 定义partition函数
        def partition(nums, l, r, x):
            i = l
            j = r

            while i < j:
                while i < j and nums[j] >= x:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1

                while i < j and nums[i] <= x:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1

            nums[i] = x
            return i

        index1 = partition(nums, 0, n - 1, 1)
        index2 = partition(nums, index1 + 1, n - 1, 2)
        return nums


if __name__ == '__main__':
    nums1 = [1, 2, 0, 0, 1, 2]
    solution = Solution()
    print(solution.sort(nums1, len(nums1)))