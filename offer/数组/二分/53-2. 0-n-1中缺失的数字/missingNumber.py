# -*- coding = utf-8 -*-

class Solution:

    def missingNumber(self, nums):
        """
        例如长度为3,内容为0~3,求缺失值
        :param nums:
        :return:
        """
        # 1. 特殊情况：题干说明数组不为空

        # 2. 初始化左右指针
        L = 0
        R = len(nums) - 1

        # 3. 算法流程：
        while L <= R:   # 此时可以让L越过R或者让R越过L
            mid = (L + R) // 2
            if nums[mid] == mid:    # 此时缺失值应该在mid右侧
                L = mid + 1
            else:                   # 此时缺失值应该在mid左侧，假如mid-1对应值==mid-1，只要L=mid+1越界就好了
                R = mid - 1
        return L


if __name__ == '__main__':
    test1 = [0, 1, 3]       # 对于缺失中间值的都不需要L==R遍历；主要应对开头缺失和结尾缺失
    test2 = [0,1,2,3,4,5,6,7,9]
    solution = Solution()
    print(solution.missingNumber(test1))
    print(solution.missingNumber(test2))
    '''
    时间复杂度：logn
    空间复杂度：1
    '''