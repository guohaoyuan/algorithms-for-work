# -*- coding = utf-8 -*-

class Solution:

    def findRepeatNumber(self, nums):
        """
        题干要求数组长度>=2，且是长度为n，范围为0～n-1
        修改原始输入
        :param nums:
        :return: 返回任意一个重复的元素
        """
        # 1. 特殊情况：长度已经为2


        # 2. 初始化

        # 3. 算法流程
        for i in range(len(nums)):
            # 对于每个元素为其找到对应位置，并判断是否与对应位置相等
            while nums[i] != i:
                tmp = nums[i]
                if nums[i] == nums[tmp]:
                    return tmp
                else:
                    nums[i], nums[tmp] = nums[tmp], nums[i]
            if nums[i] == i:
                continue
        return
if __name__ == '__main__':
    test1 = [2, 3, 1, 0, 2, 5, 3]
    solution = Solution()
    print(solution.findRepeatNumber(test1))
    '''
    时间复杂度：n，虽然for循环下嵌套了while，但是均摊时间复杂度仍为n，
    因为如果某个位置while循环次数多，则在其后面几次循环次数较少，也就说，糟糕情况不会一直出现
    空间复杂度：1，原地修改
    '''