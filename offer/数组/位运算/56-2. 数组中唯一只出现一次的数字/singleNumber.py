# -*- coding = utf-8 -*-

class Solution(object):

    def singleNumber(self, nums):
        """
        要求时间复杂度n，空间复杂度1
        :param nums:
        :return:
        """
        # 1. 特殊情况:数组长度为1
        n = len(nums)

        if n < 2:
            return nums[0]

        # 2. 初始化32位的数组,返回结果res
        array = [0 for _ in range(32)]
        res = 0

        # 3. 算法流程：
        # 外层遍历每一个数字；内层到着遍历32数组
        for num in nums:
            mask = 1    # 用于或运算找到1
            for i in range(31, -1, -1):     # 从低位向高位遍历
                print(mask & num)
                if mask & num != 0:         # mask & num是二进制数，不是0/1
                    array[i] += 1

                # 无论或运算结果。都要左移
                mask <<= 1
        # 我们需要取余数，需要遍历32数组，从高到低
        for i in range(32):
            # 存在符号位，先左移
            res <<= 1
            res += array[i] % 3
        return res

    def singleNumber_v2(self, nums):
        """
        要求时间复杂度n，空间复杂度1
        :param nums:
        :return:
        """
        # 1. 特殊情况:数组长度为1
        n = len(nums)

        if n < 2:
            return nums[0]

        # 2. 初始化32位的数组,返回结果res
        array = [0 for _ in range(32)]
        res = 0

        # 3. 算法流程：
        # 外层遍历每一个数字；内层到着遍历32数组
        for num in nums:
            mask = 1    # 用于或运算找到1
            for i in range(31, -1, -1):     # 从低位向高位遍历
                if mask & num != 0:         # mask & num是二进制数，不是0/1
                    array[i] += 1

                # 无论或运算结果。都要左移
                mask <<= 1
        # print(array)
        # 我们需要取余数，需要遍历32数组，从高到低
        for i in range(32):
            # 存在符号位，先左移
            tmp = array[i] % 3
            if tmp == 1:
                res += 2 ** (31 - i)
            # print("i = {}, res = {}".format(i, res))
        return res

if __name__ == '__main__':
    test1 = [3,4,3,3]
    test2 = [9,1,7,9,7,9,7]
    solution = Solution()
    print(solution.singleNumber(test1))
    print(solution.singleNumber(test2))
    print(solution.singleNumber_v2(test1))
    print(solution.singleNumber_v2(test2))
    '''
    时间复杂度：n，尽管有32位数组，是常数级别
    空间复杂度：1
    '''