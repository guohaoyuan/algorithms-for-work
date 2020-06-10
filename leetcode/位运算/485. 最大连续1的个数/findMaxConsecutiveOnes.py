# -*- coding : utf-8 -*-

class Solution:
    def findMaxConsecutiveOnes(self, nums):

        # 1. 特殊情况，数组为空，则直接返回0
        if not nums:
            return 0

        # 2. 初始化当前统计长度，和当前最大长度
        count = 0
        max_count = 0

        # 3. 进行一次遍历，如果当前数字==1,则更新当前统计长度；否则更新当前最大长度，并count置零
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)

"""
时间复杂度：n，进行一次遍历
空间复杂度：1,
"""