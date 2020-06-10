# -*- coding : utf-8 -*-

class Solution:

    def singleNumber(self, nums):
        """
        只出现一次数字
        要求时间复杂度n，空间复杂度1
        :param nums:
        :return:
        """
        # 1. 特殊情况：数组为空，返回
        if not nums:
            return

        # 2. 初初始化res
        res = 0

        # 3. 算法流程
        for num in nums:
            res = res ^ num

        return res
