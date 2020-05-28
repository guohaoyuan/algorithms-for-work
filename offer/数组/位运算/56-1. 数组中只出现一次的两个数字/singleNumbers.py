# -*- coding = utf-8 -*-

class Solution:

    def singleNumbers(self, nums):
        """
        要求时间复杂度为n，空间复杂度1,找出两个只出现一次的数
        :param nums:
        :return:
        """

        # 1. 特殊情况，题干要求长度>=2

        # 2. 初始化两个数字，全体异或结果
        a = 0
        b = 0
        ret = 0

        # 3. 算法流程
        # 求得全体异或结果
        for num in nums:
            ret ^= num

        # 找到不为1的位
        h = 1
        while h & ret == 0:
            h = h << 1

        # 分组异或
        for num in nums:
            if num & h == 0:    # 对应位=0
                a ^= num
            else:               # 对应位！=0
                b ^= num
        return [a, b]

if __name__ == '__main__':
    test1 = [4, 1, 4, 6]
    test2 = [1, 2, 10, 4, 1, 4, 3, 3]
    solution = Solution()
    print(solution.singleNumbers(test1))
    print(solution.singleNumbers(test2))