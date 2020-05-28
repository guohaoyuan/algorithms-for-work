# -*- coding = utf-8 -*-

class Solution(object):

    def getNumberSameAsIndex(self, nums):
        """

        :param nums:
        :return:
        """
        # 1. 特殊情况：数组为空
        if not nums:
            return

        # 2. 初始化左右指针
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == mid:
                return mid
            elif nums[mid] > mid:
                # 则右侧的都大于对应索引
                R = mid - 1
            else:
                # 则左侧的都小于对应的索引
                L = mid + 1

        return -1

if __name__ == '__main__':
    test1 = [-3, -1, 1, 3, 5]
    solution = Solution()
    print(solution.getNumberSameAsIndex(test1))