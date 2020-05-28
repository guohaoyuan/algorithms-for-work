# -*- coding = utf-8 -*-

class Solution(object):

    def singleNumber(self, nums):
        """
        要求现行时间复杂度，不使用额外空间
        :param nums:
        :return: 返回重复的数字
        """

        # 1. 特殊情况：数组不为空

        # 2. 初始化返回结果变量
        res = 0 # 任何数异或0=本身

        # 3. 算法流程：
        for num in nums:
            res = res ^ num
            # print(res)
        return res


if __name__ == '__main__':
    test1 = [2, 2, 1]
    test2 = [4, 1, 2, 1, 2]
    solution = Solution()
    print(solution.singleNumber(test1))
    print(solution.singleNumber(test2))
    '''
    时间复杂度：n，从头到尾遍历一次数组
    空间复杂度：1，常数级别的变量
    '''