# -*- coding = utf-8 -*-

class Solution(object):

    def twoSum(self, nums, target):
        """
        立刻想到暴力解法，固定一个数，遍历数组，时间复杂度为n**2；不理想我们考虑双指针
        :param nums:
        :param target:
        :return:
        """
        # 1. 特殊情况：长度不足2
        n = len(nums)

        if n < 2:
            return

        # 2. 初始化左右指针LR
        L = 0
        R = n - 1

        # 3. 算法流程
        while L < R:
            # 首先考虑结束条件
            if nums[L] + nums[R] == target:
                return [nums[L], nums[R]]
            elif nums[L] + nums[R] > target:    # 说明太大了，左移右指针
                R -= 1
            else:                               # 说明太小了，右移左指针
                L += 1
        return  # 没找到

if __name__ == '__main__':
    test1 = [2, 7, 11, 15]
    target1 = 9
    test2 = [10, 26, 30, 31, 47, 60]
    target2 = 40
    solution = Solution()
    print(solution.twoSum(test1, target1))
    print(solution.twoSum(test2, target2))
    '''
    时间复杂度：n，因为遍历一次数组
    空间复杂度：1，因为常数级别的变量
    '''