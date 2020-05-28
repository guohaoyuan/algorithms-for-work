# -*- coding = utf-8 -*-

class Solution:

    def exchange(self, nums):
        """
        将奇数放在前面，偶数放在后面
        是否在原地修改
        立刻想到用一个辅助数组，将偶数放在前面，奇数放在后面，也是双指针
        :param nums: 输入数组
        :return: 返回修改数组
        """
        # 1. 特殊情况:题干规定长度从1开始
        # if not nums:
        #     return nums
        #
        # 2. 初始化左右指针
        L = 0
        R = len(nums) - 1

        # 3. 算法流程
        while L < R:
            while L < R and nums[L] & 1 == 1:   # 是奇数
                L += 1

            while L < R and nums[R] & 1 == 0:   # 是偶数
                R -= 1

            nums[L], nums[R] = nums[R], nums[L]

        return nums

if __name__ == '__main__':
    test1 = [1, 2, 3, 4]
    solution = Solution()
    print(solution.exchange(test1))
    '''
    时间复杂度：n 可以看出双指针不同与二分法，时间复杂度都不一样
    空间复杂度：1 原地修改
    '''