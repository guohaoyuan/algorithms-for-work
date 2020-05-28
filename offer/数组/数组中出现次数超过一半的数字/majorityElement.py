# -*- coding = utf-8 -*-

class Solution:

    def majorityElement(self, nums):
        # 1. 数组长度>=1

        # 2. 初始化第一个数， 票数
        x = nums[0]
        votes = 1

        # 3. 算法流程
        for i in range(1, len(nums)):
            if votes == 0:
                x = nums[i]
                votes = 1

            if nums[i] == x:
                votes += 1
            else:
                votes -= 1
        return x

if __name__ == '__main__':
    test1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution = Solution()
    print(solution.majorityElement(test1))
    '''
    时间复杂度：n
    空间复杂度：1 原地修改
    '''